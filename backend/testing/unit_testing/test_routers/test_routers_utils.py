from routers.utils import (serialize_tool_calls, deserialize_tool_calls, 
                    insert_messages, fetch_messages)
from testing.unit_testing.data import (chat_id, db_data_in, db_data_out, 
                                                    db_data_raw, serialized_tool_calls, 
                                                    tool_calls)
from databases.message_db.queries import q_insert_message, q_messages


def test_serialize_tool_calls():
    assert serialize_tool_calls(tool_calls) == serialized_tool_calls

def test_deserialize_tool_calls():
    assert deserialize_tool_calls(serialized_tool_calls) == tool_calls


def test_insert_messages(mocker):
    cur = mocker.Mock()
    insert_messages(cur, db_data_raw, chat_id)
    cur.executemany.assert_called_once_with(q_insert_message, db_data_in)

def test_fetch_messages(mocker):
    cur = mocker.Mock()
    cur.fetchall.return_value = db_data_out
    assert fetch_messages(cur, chat_id) == db_data_raw
    cur.execute.assert_called_once_with(q_messages, (chat_id,))

