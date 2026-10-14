from agent_core.agent import Agent, Role
from ollama import Message
from testing.unit_testing.data import (response, pre_conversation, tool_response, 
                                       string, response_no_tools)
import pytest

def dummy_tool1(a1, a2, a3, a4):
    return "tool_result"

def dummy_tool2():
    return None

def dummy_tool3():
    raise Exception("er ging iets fout")

@pytest.fixture
def agent():
    return Agent(model="model_naam", 
                  tools=[dummy_tool1, dummy_tool2, dummy_tool3],
                  system_prompt="S",
                  max_rounds=2)


def test_agent_constructor(agent):
    assert agent.model == "model_naam"
    assert agent.tools == [dummy_tool1, dummy_tool2, dummy_tool3]
    assert agent.tools_map == {
        "dummy_tool1": dummy_tool1,
        "dummy_tool2": dummy_tool2,
        "dummy_tool3": dummy_tool3
    }
    assert agent.system_prompt == string
    assert agent.max_rounds == 2

def test_agent_execute_tools(agent):
    messages = []
    agent._execute_tools(response, messages) 
    assert messages == tool_response

def test_agent_chat(agent, mocker):
    mock_ollama = mocker.patch("agent_core.agent.ollama")
    mock_ollama.chat.return_value = response

    # Test of system en user prompt toegevoegd worden.
    agent.max_rounds = 0
    assert agent.chat([], user_prompt=string) == [
        *pre_conversation,
        {
            "role": "assistant",
           "content": "Sorry, ik kon de opdracht niet uitvoeren."
        }
    ]

    # Test of tool calls correct aangeroepen en toegevoegd worden.
    agent.max_rounds = 1
    assert agent.chat([], user_prompt=string) == [
            *pre_conversation,
             {
                "role": response.message.role,
                "content": response.message.content,
                "tool_calls": response.message.tool_calls
            },
            *tool_response,
              {"role": "assistant",
               "content": "Sorry, ik kon de opdracht niet uitvoeren."}
        ]

    # Test of loop onderbroken wordt bij een eindantwoord.
    agent.max_rounds = 2
    mock_ollama.chat.return_value = response_no_tools
    assert agent.chat([], user_prompt = string) == [
        *pre_conversation,
        {
            "role": response_no_tools.message.role,
            "content": response_no_tools.message.content,
            "tool_calls": response_no_tools.message.tool_calls
        }
    ]