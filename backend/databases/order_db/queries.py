# Haalt alle klanten op, inclusief de naam van hun aanbrenger.
q_klanten = """
SELECT K1.nr, K1.naam, K1.aanbrenger, K2.naam
FROM Klant K1
LEFT OUTER JOIN Klant K2 ON K1.aanbrenger = K2.nr
"""

# Haalt alle orders op, inlcusief het totaalbedrag van de order.
q_orders = """
SELECT O.nr, O.klant, O.datum, 
        ROUND(SUM(COALESCE(Orl.aantal * A.verkoopprijs, 0)), 2)
FROM Order_ O
LEFT JOIN Orderregel Orl ON O.nr = Orl.order_
LEFT JOIN Artikel A ON Orl.artikel = A.nr
WHERE O.klant = ?
GROUP BY O.nr, O.klant, O.datum
ORDER BY datum
"""

#Haalt alle orderregels op, inclusief het bedrag van de orderregel.
q_orderregels = """
SELECT Orl.order_, Orl.volgnr, Orl.artikel, Orl.aantal, 
        A.omschrijving, ROUND(Orl.aantal * A.verkoopprijs, 2)
FROM Orderregel Orl
JOIN Artikel A ON Orl.artikel = A.nr
WHERE Orl.order_ = ?
ORDER BY Orl.volgnr
"""

