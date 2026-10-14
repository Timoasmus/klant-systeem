from agent_core.tools.utils import query_db

def get_klanten(nr: int | None = None, naam: str | None = None,
                aanbrenger: int | None = None) -> list[dict]:
    """Geeft tabel 'Klant' terug.

    Args:
        nr: Optioneel. Filtert op klantnummer.
        naam: Optioneel. Filtert op klantnaam.
        aanbrenger: Optioneel. Filtert op aanbrenger van de klant.

    Returns:
        Alle (geselecteerde) klanten (nr, naam, aanbrenger)
    """
    args = [(k, v) for k, v in locals().items() if v is not None]
    return query_db('Klant', args)


def get_orders(nr: int | None = None, klant: int | None = None,
               datum: str | None = None) -> list[dict]:
    """Geeft tabel 'Order_' terug.

    Args:
        nr: Optioneel. Filtert op ordernummer.
        klant: Optioneel. Filtert op klantnummer.
        datum: Optioneel. Filtert op datum (YYYY-MM-DD).

    Returns:
      Alle (geselecteerde) orders (nr, klant, datum)
    """
    args = [(k, v) for k, v in locals().items() if v is not None]
    return query_db('Order_', args)


def get_artikelen(nr: int | None = None, omschrijving: str | None = None,
                  verkoopprijs: float | None = None, inkoopprijs: float | None = None,
                  voorraad: int | None = None) -> list[dict]:
    """Geeft tabel 'Artikel' terug. 

    Args:
        nr: Optioneel. Filtert op artikelnummer.
        omschrijving: Optioneel. Filtert op artikelomschrijving.
        verkoopprijs: Optioneel. Filtert op verkoopprijs.
        inkoopprijs: Optioneel. Filtert op inkoopprijs.
        voorraad: Optioneel. Filtert op beschikbare voorraad.

    Returns:
      Alle (geselecteerde) artikelen (nr, omschrijving, verkoopprijs, inkoopprijs, voorraad)
    """
    args = [(k, v) for k, v in locals().items() if v is not None]
    return query_db('Artikel', args)


def get_orderregels(order_: int | None = None, volgnr: int | None = None,
                    artikel: int | None = None, aantal: int | None = None) -> list[dict]:
    """Geeft tabel 'Orderregel' terug.

    Args:
        order_: Optioneel. Filtert op nummer van bijbehorende order.
        volgnr: Optioneel. Filtert op numering binnen een order.
        artikel: Optioneel. Filtert op artikelnummer.
        aantal: Optioneel. Filtert op aantal keer dat het product besteld is.

    Returns:
        Alle (geselecteerde) orderregels (order_, volgnr, artikel, aantal)
    """
    args = [(k, v) for k, v in locals().items() if v is not None]
    return query_db('Orderregel', args)