import ollama
from enum import StrEnum
from collections.abc import Callable
import logging 

logger = logging.getLogger()

class Role(StrEnum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    TOOL = "tool"


class Agent:
    """
    Stateless wrapper die configuraties van een agent bijhoudt, met een enkele methode
    'chat' die een user prompt afhandelt, waarbij de berichtgeschiedenis buiten de klasse 
    bewaard wordt.
    """
    def __init__(
            self, 
            model: str, 
            tools: list[Callable] | None = None,
            system_prompt: str | None = None, 
            max_rounds: int = 5
    ):
        """
        Initialiseert agent met bijbehorende configuratie.
        
        Parameters:
            - model: naam van het model
            - tools (optioneel): lijst met functies die het model mag gebruiken
            - system_prompt (optioneel): systeemprompt die aan het begin van het 
                gesprek toegevoegt wordt
            - max_rounds: het aantal keer dat de agent een poging mag doen om tot
                een eindantwoord te komen 
        """

        self.model = model
        self.tools = tools
        if tools:
            self.tools_map = {tool.__name__: tool for tool in tools}
        self.max_rounds = max_rounds
        self.system_prompt = system_prompt

    def chat(
            self, 
            messages: list[dict], 
            user_prompt: str
    ) -> list[dict]:
        
        """
        Handelt conversatie en tool calls af, waarbij het de lijst met berichten
        uitbreidt. Stopt als de agent geen tool_calls meer aanroept, of het maximaal
        aantal rondes bereikt is.

        Parameters:
            - messages: berichtgeschiedenis
            - user_prompt: nieuwe prompt vanuit de gebruiker
        """

        if not messages and self.system_prompt:
            messages.append({
                "role": Role.SYSTEM,
                "content": self.system_prompt
            })

        messages.append({
            "role": Role.USER,
            "content": user_prompt
            })
        
        for _ in range(self.max_rounds):
            response = ollama.chat(
                model=self.model,
                messages=messages,
                tools=self.tools,
                options={"temperature": 0},
            )
           
            messages.append({
                "role": Role.ASSISTANT,
                "content": response.message.content,
                "tool_calls": response.message.tool_calls
            })

            if not response.message.tool_calls:
                return messages

            self._execute_tools(response, messages)

        messages.append({
            "role": Role.ASSISTANT,
            "content": "Sorry, ik kon de opdracht niet uitvoeren."
        })
        return messages
    
    def _execute_tools(self, response, messages):
        for tool_call in response.message.tool_calls:
            function_name = tool_call.function.name
            arguments = tool_call.function.arguments

            try:
                function = self.tools_map.get(function_name)
                result = function(**arguments)
            except Exception as e:
                result = f"Tool execution failed: {e}"

            messages.append({
                "role": Role.TOOL,
                "content": str(result) if result else "Geen resultaten"
            })

