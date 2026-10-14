import sqlite3
from pathlib import Path

# Hulpfunctie voor het queryen van de database, waarbij argumenten ingevuld door de
# database agent verwerkt worden in een geconcateneerde WHERE-clausule.
def query_db(table: str, args: list[tuple[str, object]]) -> list[dict]:
    query = f"""
    SELECT *
    FROM {table}
    """
    path = Path(__file__).parent.parent.parent / "databases" / "order_db" / "order.db"
    with sqlite3.connect(path) as con:
        con.row_factory = sqlite3.Row
        con.execute("PRAGMA foreign_keys = ON")
        cur = con.cursor()
        if not args:
            cur.execute(query)
            return [dict(row) for row in cur.fetchall()]

        conditions = []
        values = []
        for k, v in args:
            values.append(v)
            if isinstance(v, str):
                conditions.append(f"LOWER({k}) = LOWER(?)")
            else:
                conditions.append(f"{k} = ?")

        query += f"WHERE {' AND '.join(conditions)}"
        cur.execute(query, values)
        return [dict(row) for row in cur.fetchall()]