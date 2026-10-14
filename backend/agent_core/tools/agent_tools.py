from dotenv import load_dotenv
import os
from agent_core.prompts import SYSTEM_PROMPT_DB
from agent_core.agent import Agent
from agent_core.tools.db_agent_tools import (get_artikelen, get_klanten, 
                                             get_orderregels, get_orders)

load_dotenv(override=True)


tools = [get_orderregels, get_artikelen, get_orders, get_klanten]
db_agent = Agent(
    model=os.getenv("MODEL"),
    tools=tools,
    system_prompt=SYSTEM_PROMPT_DB,
    max_rounds=6
)


def question_database(vraag: str) -> str:
    """Stelt een vraag aan de database specialist agent.

    Args:
        vraag: De vraag die de database agent moet beantwoorden.

    Returns:
        Antwoord op de vraag, als deze gevonden is.
    """
    return db_agent.chat([], user_prompt=vraag)[-1]["content"]

        