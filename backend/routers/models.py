from pydantic import BaseModel

# Data-modellen
class Klant(BaseModel):
    nr: int
    naam: str 
    aanbrenger: int | None = None 

class Order(BaseModel):
    nr: int
    klant: int 
    datum: str 

class Artikel(BaseModel):
    nr: int 
    omschrijving: str 
    verkoopprijs: float
    inkoopprijs: float 
    voorraad: int 

class Orderregel(BaseModel):
    order_: int 
    volgnr: int 
    artikel: int 
    aantal: int 


# Data-modellen voor data_router
class GetKlant(Klant):
    aanbrenger_naam: str | None = None

class GetOrder(Order):
    totaalbedrag: float
    
class GetOrderregel(Orderregel):
    artikel_omschrijving: str 
    bedrag: float


# Data-modellen voor agent_router
class ChatMessage(BaseModel):
    chat_id: str | None = None
    content: str