"""
Bookly - Storage Layer
Starts with local SQLite for fast testing. Swap save_booking() internals
to write to Google Sheets later without touching the rest of the app.
"""

import sqlite3
from datetime import datetime

DB_PATH = "bookings.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT,
            time_slot TEXT,
            customer_name TEXT,
            phone TEXT,
            created_at TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_booking(service: str, time_slot: str, customer_name: str, phone: str):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO bookings (service, time_slot, customer_name, phone, created_at) VALUES (?, ?, ?, ?, ?)",
        (service, time_slot, customer_name, phone, datetime.now().isoformat()),
    )
    conn.commit()
    conn.close()


def get_all_bookings():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.execute("SELECT id, service, time_slot, customer_name, phone, created_at FROM bookings ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return [
        {"id": r[0], "service": r[1], "time": r[2], "name": r[3], "phone": r[4], "created_at": r[5]}
        for r in rows
    ]


init_db()
