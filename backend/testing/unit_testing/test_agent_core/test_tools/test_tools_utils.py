from agent_core.tools.utils import query_db

def test_query_db(mocker):
    connect = mocker.patch("agent_core.tools.utils.sqlite3.connect")
    con = connect.return_value.__enter__.return_value
    cur = con.cursor.return_value

    query = """
    SELECT *
    FROM Tabel
    """

    query_db(table="Tabel", args=[]) 
    con.execute.assert_called_once_with("PRAGMA foreign_keys = ON")
    cur.execute.assert_called_with(query)
    cur.fetchall.assert_called()

    args = [("A1", "S"), ("A2", 1), ("A3", 1.1)]
    values = ["S", 1, 1.1]

    query_with_selection = """
    SELECT *
    FROM Tabel
    WHERE LOWER(A1) = LOWER(?) AND A2 = ? AND A3 = ?"""
    
    query_db(table="Tabel", args=args)
    cur.execute.assert_called_with(query_with_selection, values)
    cur.fetchall.assert_called()