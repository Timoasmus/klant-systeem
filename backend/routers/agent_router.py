from fastapi import APIRouter, Depends
from sqlite3 import Connection
import logging
from dotenv import load_dotenv
import os
import uuid

from routers.models import ChatMessage
from routers.utils import fetch_messages, insert_messages, raise_http500

from agent_core.agent import Agent
from agent_core.tools.agent_tools import question_database
from agent_core.prompts import SYSTEM_PROMPT

from databases.db_connection import get_message_db
from databases.message_db.queries import q_insert_chat


load_dotenv(override=True)

logger = logging.getLogger(__name__)

agent_router = APIRouter()

agent = Agent(
    model=os.getenv("MODEL"),
    tools=[question_database],
    system_prompt=SYSTEM_PROMPT,
    max_rounds=2
)


@agent_router.post("/chat",
                   description="Chat met de agent met betreffende chatgeschiedenis.",
                   response_model=ChatMessage)
def chat(user_message: ChatMessage, db: Connection = Depends(get_message_db)):
    try:
        cur = db.cursor()

        chat_id = user_message.chat_id
        if not chat_id:
            chat_id = str(uuid.uuid4())
            cur.execute(q_insert_chat, (chat_id,))
            message_history = []
        else:
            message_history = fetch_messages(cur, chat_id)

        old_count = len(message_history)
        response = agent.chat(message_history, user_message.content)[old_count:]

        insert_messages(cur, response, chat_id)
        db.commit()

        return ChatMessage(
            chat_id=chat_id,
            content=response[-1]["content"]
        )

    except Exception as e:
        raise_http500(e, logger, db)
