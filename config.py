# Bookly - Business Configuration
# Swap this file per client to reuse the same booking engine for any business.

BUSINESS = {
    "name": "FitZone Gym",
    "greeting": "Hi! Welcome to FitZone Gym 💪 How can I help you today?",
    "services": [
        {"id": "trial", "name": "Free Trial Session", "duration": "1 hour", "price": "Free"},
        {"id": "personal_training", "name": "Personal Training Session", "duration": "1 hour", "price": "₹500/session"},
        {"id": "membership_1m", "name": "1 Month Membership", "duration": "1 month", "price": "₹1500"},
        {"id": "membership_3m", "name": "3 Month Membership", "duration": "3 months", "price": "₹4000"},
    ],
    "timings": "Mon-Sat, 6 AM - 10 PM (closed Sundays)",
    "location": "Gomti Nagar, Lucknow",
    "faqs": {
        "price": "Our 1-month membership is ₹1500, 3-month is ₹4000. Personal training is ₹500/session. First trial session is free!",
        "timing": "We're open Monday to Saturday, 6 AM to 10 PM. Closed on Sundays.",
        "location": "We're located in Gomti Nagar, Lucknow.",
    }
}
