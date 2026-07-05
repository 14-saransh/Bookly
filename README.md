# Bookly

A simple booking assistant for small businesses like gyms, salons, and tuition centers. Customers chat with it to check services, pricing, and timings, and book a slot, no phone calls or manual back and forth needed.

**Live demo:** https://bookly-eour.onrender.com

## Why I built this

Most small businesses in Tier 2 cities handle bookings manually over WhatsApp or phone calls, which eats up time and often means missed messages. Bookly automates that basic conversation so business owners can focus on actually running their business, while customers get instant replies.

## How it works

The bot follows a simple conversation flow: greet the customer, show available services, ask for a preferred time, collect name and phone number, then confirm the booking. It also answers quick questions about pricing, timing, and location directly. Every confirmed booking gets saved so the business owner has a record of who's coming in and when.

The whole thing is built to be reused across different businesses. One config file holds all the business-specific details (name, services, prices, timings), so setting it up for a new client is just a matter of editing that file, not rebuilding the app.

## Tech stack

- **Backend:** Python, FastAPI
- **Frontend:** HTML/CSS/JavaScript (lightweight chat widget, no framework needed)
- **Storage:** SQLite
- **Deployment:** Render

## Running it locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open `widget.html` in your browser.

## What's next

- Sync bookings to Google Sheets so business owners can view them without touching any code
- WhatsApp integration so the bot works where small business owners already are
- A simple dashboard for viewing and managing bookings
