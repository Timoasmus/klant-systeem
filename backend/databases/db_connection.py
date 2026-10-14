import sqlite3
from pathlib import Path

def get_db(path: str):
    con = sqlite3.connect(path, check_same_thread=False)
    con.execute("PRAGMA foreign_keys = ON")

    try:
        yield con
    finally:
        con.close()

def get_order_db():
    path = Path(__file__).parent / "order_db" / "order.db"
    yield from get_db(str(path))

def get_message_db():
    path = Path(__file__).parent / "message_db" / "message.db"
    yield from get_db(str(path))