from sqlite3 import Cursor, Connection
import json 
from ollama import Message
from logging import Logger
from fastapi import HTTPException, status

from databases.message_db.queries import q_messages, q_insert_message

from agent_core.agent import Role

# Haalt alle berichten van een chat uit de database, en formateert ze zodat ze 
# aan de LLM gegeven kunnen worden.
def fetch_messages(cur: Cursor, chat_id: str) -> list[dict]:
    cur.execute(q_messages, (chat_id,))
    messages = []

    for role, content, tool_calls in cur.fetchall():
        message = {
            "role": role,
            "content": content
        }

        if role == Role.ASSISTANT:
            message["tool_calls"] = deserialize_tool_calls(json.loads(
                tool_calls)) if tool_calls else None

        messages.append(message)

    return messages

# Hulpfunctie die tool_calls van json vorm naar klasse vorm omzet.
def deserialize_tool_calls(tool_calls: list[dict]) -> list[Message.ToolCall]:
    return [
        Message.ToolCall(
            function=Message.ToolCall.Function(
                name=tc["function"]["name"], 
                arguments=tc["function"]["arguments"]
            )
        ) for tc in tool_calls
    ]


# Zet alle nieuw gegenereerde berichten van een chat in de database, zodat ze
# later weer opgehaald kunnen worden.
def insert_messages(cur: Cursor, response: list[dict], chat_id: str) -> None:
    new_messages = []

    for message in response:
        tool_calls = message.get("tool_calls")

        new_messages.append((
            chat_id,
            message["role"],
            message["content"],
            json.dumps(serialize_tool_calls(tool_calls)) 
                if tool_calls else None
        ))

    cur.executemany(q_insert_message, new_messages)

# Hulpfunctie die tool_calls van klasse vorm naar json vorm omzet.
def serialize_tool_calls(tool_calls: list[Message.ToolCall]) -> list[dict]:
    return [
        {
            "function": {
                "name": tc.function.name,
                "arguments": tc.function.arguments
            }
        }
        for tc in tool_calls
    ]


# Hulpfunctie die een error in een endpoint afhandelt.
def raise_http500(e: Exception, logger: Logger = None, db: Connection = None):
    if logger:
        logger.exception(e)
    if db:
        db.rollback()
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=f"Something went wrong: {str(e)}")