from routers.data_router import get_orderregels, get_klanten, get_orders
from routers.models import GetOrderregel, GetKlant, GetOrder
from databases.order_db.queries import q_orderregels, q_klanten, q_orders

def test_get_klanten(mocker):
    cur = mocker.Mock()
    cur.fetchall.return_value = [
        (1, "S", 1, "S")
    ]

    db = mocker.Mock()
    db.cursor.return_value = cur 

    result = get_klanten(db)

    cur.execute.assert_called_once_with(q_klanten)
    assert result == [
        GetKlant(
            nr=1,
            naam="S",
            aanbrenger=1,
            aanbrenger_naam="S"
        )
    ]

def test_get_orders(mocker):
    cur = mocker.Mock()
    cur.fetchall.return_value = [
        (1, 1, "S", 1.0)
    ]

    db = mocker.Mock()
    db.cursor.return_value = cur 

    result = get_orders(2, db)

    cur.execute.assert_called_once_with(q_orders, (2,))
    assert result == [
        GetOrder(
            nr=1,
            klant=1,
            datum="S",
            totaalbedrag=1.0
        )
    ]

def test_get_orderregels(mocker):
    cur = mocker.Mock()
    cur.fetchall.return_value = [
        (1, 1, 1, 1, "S", 1.0)
    ]

    db = mocker.Mock()
    db.cursor.return_value = cur

    result = get_orderregels(2, db)

    cur.execute.assert_called_once_with(q_orderregels, (2,))
    assert result == [
        GetOrderregel(
            order_=1,
            volgnr=1,
            artikel=1,
            aantal=1,
            artikel_omschrijving="S",
            bedrag=1.0,
        )
    ]