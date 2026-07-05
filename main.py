from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

from conversation import handle_message, get_session
from storage import save_booking, get_all_bookings
from config import BUSINESS

app = FastAPI(title="Bookly")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatMessage(BaseModel):
    session_id: str
    message: str


@app.get("/")
def root():
    return FileResponse("widget.html")


@app.get("/status")
def status():
    return {"status": "Bookly is running", "business": BUSINESS["name"]}


@app.post("/chat")
def chat(payload: ChatMessage):
    reply = handle_message(payload.session_id, payload.message)

    if reply == "booking_confirmed":
        session = get_session(payload.session_id)
        data = session["data"]
        save_booking(
            service=data.get("service", ""),
            time_slot=data.get("time", ""),
            customer_name=data.get("name", ""),
            phone=data.get("phone", ""),
        )
        reply = f"✅ Booking confirmed! We'll see you then, {data.get('name', '')}. See you at {BUSINESS['name']}!"

    return {"reply": reply}


@app.get("/bookings")
def bookings():
    return {"bookings": get_all_bookings()}
