import sqlite3

con = sqlite3.connect("order.db")
cur = con.cursor()

klanten = [
    (1, "Jan Jansen", None),
    (2, "Piet Pieters", 1),
    (3, "Anne de Vries", 1),
    (4, "Kees Smit", 2),
    (5, "Lisa Bakker", 2),
    (6, "Mark Visser", 3),
    (7, "Sophie Mulder", None),
    (8, "Tom de Boer", 3)
]

cur.executemany("""
    INSERT INTO Klant (nr, naam, aanbrenger)
    VALUES (?, ?, ?)
""", klanten)

artikelen = [
    (1, "Laptop", 899.99, 650.00, 10),
    (2, "Muis", 24.95, 12.00, 50),
    (3, "Toetsenbord", 49.95, 25.00, 30),
    (4, "Monitor", 249.99, 150.00, 15),
    (5, "USB-kabel", 9.95, 3.50, 100),
    (6, "Webcam", 59.95, 30.00, 20),
    (7, "Headset", 79.95, 40.00, 25),
    (8, "Luidsprekers", 69.95, 35.00, 18),
    (9, "Printer", 159.99, 100.00, 8),
    (10, "SSD 1TB", 89.95, 55.00, 12),
    (11, "USB-stick", 14.95, 6.00, 75),
    (12, "Laptopstand", 39.95, 20.00, 22),
    (13, "HDMI-kabel", 12.95, 5.00, 60),
    (14, "Microfoon", 99.95, 55.00, 10),
    (15, "Tablet", 299.99, 200.00, 7)
]

cur.executemany("""
    INSERT INTO Artikel
        (nr, omschrijving, verkoopprijs, inkoopprijs, voorraad)
    VALUES (?, ?, ?, ?, ?)
""", artikelen)

orders = [
    (1, 1, "2026-09-01"),
    (2, 2, "2026-09-02"),
    (3, 1, "2026-09-03"),
    (4, 3, "2026-09-05"),
    (5, 4, "2026-09-07"),
    (6, 2, "2026-09-10"),
    (7, 5, "2026-09-12"),
    (8, 6, "2026-09-15"),
    (9, 1, "2026-09-18"),
    (10, 8, "2026-09-20")
]

cur.executemany("""
    INSERT INTO Order_ (nr, klant, datum)
    VALUES (?, ?, ?)
""", orders)

orderregels = [
    (1, 1, 1, 1),
    (1, 2, 2, 2),
    (1, 3, 5, 3),

    (2, 1, 4, 1),
    (2, 2, 6, 1),

    (3, 1, 3, 1),
    (3, 2, 7, 1),
    (3, 3, 13, 2),

    (4, 1, 2, 1),
    (4, 2, 8, 2),
    (4, 3, 11, 5),

    (5, 1, 9, 1),
    (5, 2, 13, 2),

    (6, 1, 10, 1),
    (6, 2, 12, 1),
    (6, 3, 5, 2),

    (7, 1, 15, 1),
    (7, 2, 7, 1),

    (8, 1, 14, 1),
    (8, 2, 2, 1),

    (9, 1, 1, 1),
    (9, 2, 4, 2),
    (9, 3, 10, 1),

    (10, 1, 6, 1),
    (10, 2, 11, 3),
    (10, 3, 13, 1)
]

con.execute("PRAGMA foreign_keys = ON")

cur.executemany("""
    INSERT INTO Orderregel
        (order_, volgnr, artikel, aantal)
    VALUES (?, ?, ?, ?)
""", orderregels)

con.commit()