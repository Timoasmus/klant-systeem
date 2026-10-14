import sqlite3

con = sqlite3.connect("message.db")
cur = con.cursor()

roles = [
    ("user",),
    ("assistant",),
    ("system",),
    ("tool",)
]

con.execute("PRAGMA foreign_keys = ON")

cur.executemany("""
    INSERT INTO Role (role)
    VALUES (?)
""", roles)

con.commit()