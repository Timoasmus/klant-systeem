import sqlite3

con = sqlite3.connect("message.db")
cur = con.cursor()

#Role [role]
create_role = """
CREATE TABLE Role (
    role TEXT NOT NULL,
    PRIMARY KEY (role) 
);
"""

#Chat [id | created_at]
create_chat = """
CREATE TABLE Chat (
    id TEXT NOT NULL, 
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
)
"""

#Message [id | chat_id | created_at | role | content | tool_calls]
create_message = """
CREATE TABLE Message (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,   
    chat_id TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (STRFTIME('%Y-%m-%d %H:%M:%f', 'now')),
    role TEXT NOT NULL,
    content TEXT,
    tool_calls TEXT,
    FOREIGN KEY (role)
        REFERENCES Role(role)
        ON UPDATE CASCADE,
    FOREIGN KEY (chat_id)
        REFERENCES Chat(id)
        ON DELETE CASCADE
);
"""

con.execute("PRAGMA foreign_keys = ON")
cur.execute(create_role)
cur.execute(create_chat)
cur.execute(create_message)

con.commit()