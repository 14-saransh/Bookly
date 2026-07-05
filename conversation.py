"""
Bookly - Conversation Engine
A simple state-machine based chat flow for booking appointments.
No LLM needed for the core flow (keeps it fast, free, and predictable).
An LLM layer can be added later for handling free-form FAQ-style questions.
"""

from config import BUSINESS

# In-memory session store: {session_id: {"state": ..., "data": {...}}}
sessions = {}


def get_session(session_id: str):
    if session_id not in sessions:
        sessions[session_id] = {"state": "start", "data": {}}
    return sessions[session_id]


def reset_session(session_id: str):
    sessions[session_id] = {"state": "start", "data": {}}


def detect_intent(message: str):
    msg = message.lower()
    if any(word in msg for word in ["price", "cost", "fee", "charges"]):
        return "faq_price"
    if any(word in msg for word in ["time", "timing", "open", "hours"]):
        return "faq_timing"
    if any(word in msg for word in ["location", "address", "where"]):
        return "faq_location"
    if any(word in msg for word in ["book", "session", "appointment", "trial", "join", "membership"]):
        return "book"
    return "unknown"


def handle_message(session_id: str, message: str) -> str:
    session = get_session(session_id)
    state = session["state"]
    data = session["data"]

    # Global FAQ handling - works from any state, doesn't derail booking flow
    intent = detect_intent(message)
    if state == "start" and intent.startswith("faq_"):
        key = intent.split("_")[1]
        return BUSINESS["faqs"].get(key, "Let me check on that for you!") + "\n\nWould you like to book a session?"

    # State machine
    if state == "start":
        if intent == "book":
            session["state"] = "choose_service"
            services_list = "\n".join(
                [f"{i+1}. {s['name']} - {s['price']} ({s['duration']})" for i, s in enumerate(BUSINESS["services"])]
            )
            return f"Great! Here are our services:\n\n{services_list}\n\nWhich one would you like? (reply with the number)"
        else:
            return BUSINESS["greeting"]

    if state == "choose_service":
        try:
            idx = int(message.strip()) - 1
            service = BUSINESS["services"][idx]
            data["service"] = service["name"]
            session["state"] = "choose_time"
            return f"Got it, {service['name']}! What date and time works for you? (e.g. 'Tomorrow 5 PM')"
        except (ValueError, IndexError):
            return "Please reply with a valid number from the list above."

    if state == "choose_time":
        data["time"] = message.strip()
        session["state"] = "get_name"
        return "Perfect. Can I get your name?"

    if state == "get_name":
        data["name"] = message.strip()
        session["state"] = "get_phone"
        return "Thanks! And your phone number so we can confirm the booking?"

    if state == "get_phone":
        data["phone"] = message.strip()
        session["state"] = "confirm"
        return (
            f"Please confirm your booking:\n\n"
            f"Service: {data['service']}\n"
            f"Time: {data['time']}\n"
            f"Name: {data['name']}\n"
            f"Phone: {data['phone']}\n\n"
            f"Reply 'yes' to confirm or 'no' to cancel."
        )

    if state == "confirm":
        if message.strip().lower() in ["yes", "y", "confirm"]:
            session["state"] = "done"
            return "booking_confirmed"  # main.py will catch this and save + reply
        else:
            reset_session(session_id)
            return "No problem, booking cancelled. Let me know if you'd like to start over!"

    if state == "done":
        reset_session(session_id)
        return handle_message(session_id, message)

    return "Sorry, I didn't get that. Could you rephrase?"
