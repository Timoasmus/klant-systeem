from routers.models import ChatMessage
from routers.agent_router import chat

from testing.unit_testing.data import db_data_raw, chat_id

from databases.message_db.queries import q_insert_chat

def test_chat(mocker):

    # Maak mocks voor functies en klassen.
    cur = mocker.Mock()

    db = mocker.Mock()
    db.cursor.return_value = cur 

    uuid = mocker.patch("routers.agent_router.uuid")
    uuid.uuid4.return_value = chat_id

    mock_fetch_messages = mocker.patch("routers.agent_router.fetch_messages")
    mock_fetch_messages.return_value = [db_data_raw[0]]
    mock_insert_messages = mocker.patch("routers.agent_router.insert_messages")

    agent = mocker.patch("routers.agent_router.agent")
    agent.chat.return_value = db_data_raw


    # Test voor goed gedrag als user wel een chat_id meegeeft.
    user_message = ChatMessage(
        chat_id=chat_id,
        content=db_data_raw[1]["content"]
    )

    assistent_message = ChatMessage(
        chat_id=chat_id,
        content=db_data_raw[-1]["content"]
    )

    assert chat(user_message, db) == assistent_message
    mock_fetch_messages.assert_called_once_with(cur, chat_id)
    agent.chat.assert_called_with(mock_fetch_messages.return_value, 
                                       user_message.content)
    mock_insert_messages.assert_called_with(cur, db_data_raw[1:], chat_id)
    db.commit.assert_called_once()


    # Test voor goed gedrag als user geen chat_id meegeeft.
    user_message = ChatMessage(
            chat_id=None,
            content=db_data_raw[1]["content"]
        )
    
    assert chat(user_message, db) == assistent_message
    cur.execute.assert_called_once_with(q_insert_chat, (chat_id,))
    agent.chat.assert_called_with([], user_message.content)
    mock_insert_messages.assert_called_with(cur, db_data_raw, chat_id)