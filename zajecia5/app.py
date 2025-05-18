import sqlite3

# Połączenie z bazą danych
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# a) Sprzedaż produktu "Laptop"
print("a) Sprzedaż produktu 'Laptop':")
cursor.execute("SELECT * FROM sales WHERE product = 'Laptop'")
for row in cursor.fetchall():
    print(row)
print("\n" + "-"*50 + "\n")

# b) Dane tylko z dni 2025-05-07 i 2025-05-08
print("b) Dane tylko z dni 2025-05-07 i 2025-05-08:")
cursor.execute("""
    SELECT * FROM sales
    WHERE date IN ('2025-05-07', '2025-05-08')
""")
for row in cursor.fetchall():
    print(row)
print("\n" + "-"*50 + "\n")

# c) Transakcje, w których cena jednostkowa przekracza 200 zł
print("c) Transakcje z ceną jednostkową > 200 zł:")
cursor.execute("SELECT * FROM sales WHERE price > 200")
for row in cursor.fetchall():
    print(row)
print("\n" + "-"*50 + "\n")

# d) Łączna wartość sprzedaży dla każdego produktu
print("d) Łączna wartość sprzedaży dla każdego produktu:")
cursor.execute("""
    SELECT product, SUM(quantity * price) AS total_sales
    FROM sales
    GROUP BY product
""")
for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]:.2f} zł")
print("\n" + "-"*50 + "\n")

# e) Dzień z największą liczbą sprzedanych sztuk
print("e) Dzień z największą liczbą sprzedanych sztuk:")
cursor.execute("""
    SELECT date, SUM(quantity) AS total_quantity
    FROM sales
    GROUP BY date
    ORDER BY total_quantity DESC
    LIMIT 1
""")
row = cursor.fetchone()
print(f"{row[0]}: {row[1]} sztuk")

# Zamknięcie połączenia
conn.close()
