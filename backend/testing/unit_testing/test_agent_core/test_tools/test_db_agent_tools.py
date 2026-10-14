from agent_core.tools.db_agent_tools import get_klanten

# Alleen de tool get_klanten wordt hier getest, aangezien de overige tools exact 
# dezelfde werking hebben.

def test_get_klanten(mocker):
    mock_query_db = mocker.patch("agent_core.tools.db_agent_tools.query_db")
    tabel = 'Klant'

    get_klanten(nr=1, naam="S", aanbrenger=1)
    mock_query_db.assert_called_with(tabel, [
        ("nr", 1), ("naam", "S"), ("aanbrenger", 1)
        ])
    
    get_klanten(naam="S")
    mock_query_db.assert_called_with(tabel, [
        ("naam", "S")
        ])
    
    get_klanten()
    mock_query_db.assert_called_with(tabel, [])

    get_klanten(aanbrenger=1)
    mock_query_db.assert_called_with(tabel, [
        ("aanbrenger", 1)
    ])

    get_klanten(nr=None, naam=None, aanbrenger=None)
    mock_query_db.assert_called_with(tabel, [])


    