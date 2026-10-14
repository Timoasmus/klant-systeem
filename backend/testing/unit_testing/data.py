from ollama import Message, ChatResponse
from agent_core.agent import Role
import json

chat_id = "1"
string = "S"

tool_calls =  [Message.ToolCall(
            function=Message.ToolCall.Function(
                name="dummy_tool1", 
                arguments={"a1": 1, "a2": 1.1, "a3": "s", "a4": True}
                )
            )
        ]


serialized_tool_calls =  [
    {
                "function": {
                    "name": "dummy_tool1",
                    "arguments": {"a1": 1, "a2": 1.1, "a3": "s", "a4": True}
                }
            }
]

db_data_raw = [
    {"role": Role.SYSTEM, "content": string},
    {"role": Role.USER, "content": string},
    {"role": Role.ASSISTANT, "content": string, "tool_calls": tool_calls},
    {"role": Role.TOOL, "content": string},
    {"role": Role.ASSISTANT, "content": string, "tool_calls": None}
]


db_data_in= [
    (chat_id, Role.SYSTEM, string, None),
    (chat_id, Role.USER, string, None),
    (chat_id, Role.ASSISTANT, string, json.dumps(serialized_tool_calls)),
    (chat_id, Role.TOOL, string, None),
    (chat_id, Role.ASSISTANT, string, None)
]

db_data_out  = [
    (Role.SYSTEM, string, None),
    (Role.USER, string, None),
    (Role.ASSISTANT, string, json.dumps(serialized_tool_calls)),
    (Role.TOOL, string, None),
    (Role.ASSISTANT, string, None)
]

response = ChatResponse(
    message=Message(
        role="assistant",
        content=string,
        tool_calls= tool_calls + 
        [
            Message.ToolCall(
                function=Message.ToolCall.Function(
                    name="dummy_tool2", 
                    arguments={}
                    )
            ),
            Message.ToolCall(
                function=Message.ToolCall.Function(
                    name="dummy_tool3",
                    arguments={}
                )
            )
        ]
    )
)

response_no_tools = ChatResponse(
    message=Message(
        role="assistant",
        content=string,
        tool_calls=None
    )
)

pre_conversation = [
    {
        "role": "system",
        "content": string
    },
    {
        "role": "user",
        "content": string
    },
]

tool_response = [
        {
            "role": "tool",
            "content": "tool_result"
        },
        {
            "role": "tool",
            "content": "Geen resultaten"
        },
        {
            "role": "tool",
            "content": "Tool execution failed: er ging iets fout"
        }
    ]

