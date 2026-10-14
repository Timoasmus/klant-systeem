from fastapi import APIRouter, Depends
from sqlite3 import Connection
import logging 

from databases.db_connection import get_order_db
from databases.order_db.queries import q_klanten, q_orderregels, q_orders
from routers.models import GetKlant, GetOrder, GetOrderregel

from routers.utils import raise_http500

logger = logging.getLogger(__name__)

data_router = APIRouter()

@data_router.get("/klanten", 
                description="Haalt alle klanten uit de database op.",
                response_model=list[GetKlant])
def get_klanten(db: Connection = Depends(get_order_db)):
    try:
        cur = db.cursor()
        cur.execute(q_klanten)
        result = cur.fetchall()
        klanten = [GetKlant(nr=nr, naam=naam, aanbrenger=aanbrenger, 
                            aanbrenger_naam=aanbrenger_naam)
                    for nr, naam, aanbrenger, aanbrenger_naam in result]
        return klanten
    
    except Exception as e:
        raise_http500(e, logger)


@data_router.get("/orders/{klant_nr}", 
                description="Haalt alle orders van de klant met nummer 'klant_nr' op.",
                response_model=list[GetOrder])
def get_orders(klant_nr: int, db: Connection = Depends(get_order_db)):
    try: 
        cur = db.cursor()
        cur.execute(q_orders, (klant_nr,))
        result = cur.fetchall()
        orders = [GetOrder(nr=nr, klant=klant, datum=datum, 
                        totaalbedrag=totaalbedrag)
                for nr, klant, datum, totaalbedrag in result]
        return orders 

    except Exception as e:
            raise_http500(e, logger)


@data_router.get("/orderregels/{order_nr}", 
                description="Haalt alle orderregels van de order met nummer 'order_nr' op.",
                response_model=list[GetOrderregel])
def get_orderregels(order_nr: int, db: Connection = Depends(get_order_db)):
    try:
        cur = db.cursor()
        cur.execute(q_orderregels, (order_nr,))
        result = cur.fetchall()
        orderregels = [GetOrderregel(order_=order_, volgnr=volgnr, artikel=artikel, 
                                    aantal=aantal, artikel_omschrijving=artikel_omschrijving,
                                    bedrag=bedrag)
                        for order_, volgnr, artikel, aantal, 
                        artikel_omschrijving, bedrag in result]
        return orderregels

    except Exception as e:
            raise_http500(e, logger)
