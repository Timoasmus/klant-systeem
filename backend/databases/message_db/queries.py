# Voegt een nieuwe chat toe.
q_insert_chat = """
INSERT INTO Chat (id)
VALUES (?) 
"""

# Voegt een nieuwe message, behorend bij een bepaalde chat, toe.
q_insert_message = """
INSERT INTO Message (chat_id, role, content, tool_calls)
VALUES (?, ?, ?, ?)
"""

# Haalt alle messages van een chat op, en sorteert ze chronologisch.
q_messages = """
SELECT role, content, tool_calls
FROM Message
WHERE chat_id = ?
ORDER BY id ASC
"""