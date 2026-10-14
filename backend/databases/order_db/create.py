import sqlite3

con = sqlite3.connect("order.db")
cur = con.cursor()

#Klant [nr | naam | aanbrenger]
create_klant = """
CREATE TABLE Klant (
    nr INTEGER NOT NULL,
    naam TEXT NOT NULL CHECK (length(naam) <= 30),
    aanbrenger INTEGER,
    PRIMARY KEY (nr),
    FOREIGN KEY (aanbrenger)
        REFERENCES Klant(nr)
        ON UPDATE CASCADE
);
"""

#Order [nr | klant | datum]
create_order_ = """
CREATE TABLE Order_ (
    nr INTEGER NOT NULL,
    klant INTEGER NOT NULL,
    datum DATE NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (nr),
    FOREIGN KEY (klant)
        REFERENCES Klant(nr)
        ON UPDATE CASCADE
);
"""

#Artikel [nr | omschrijving | verkoopprijs | inkoopprijs | voorraad]
create_artikel = """
CREATE TABLE Artikel (
    nr INTEGER NOT NULL,
    omschrijving TEXT NOT NULL CHECK (length(omschrijving) <= 20),
    verkoopprijs DOUBLE NOT NULL,
    inkoopprijs DOUBLE NOT NULL,
    voorraad INTEGER default 0 NOT NULL,
    PRIMARY KEY (nr),
    UNIQUE (omschrijving)
);
"""

#Orderregel [order_ | volgnr | artikel | aantal]
create_orderregel = """
CREATE TABLE Orderregel (
    order_ INTEGER NOT NULL,
    volgnr INTEGER NOT NULL,
    artikel INTEGER NOT NULL,
    aantal INTEGER NOT NULL,
    PRIMARY KEY (order_, volgnr),
    FOREIGN KEY (order_)
            REFERENCES Order_(nr)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
    FOREIGN KEY (artikel)
            REFERENCES Artikel(nr)
            ON DELETE CASCADE
            ON UPDATE CASCADE
);
"""

con.execute("PRAGMA foreign_keys = ON")

for q_create in [create_klant, create_order_, 
                 create_artikel, create_orderregel]:
    cur.execute(q_create)

con.commit()