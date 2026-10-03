import sqlite3

conexion = sqlite3.connect("transactions.db")
cursor = conexion.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY AUTOINCREMENT,  type TEXT, amount REAL)"
)

cursor.execute("INSERT INTO transactions (type, amount) VALUES ('deposit', 100.0)")
cursor.execute("INSERT INTO transactions (type, amount) VALUES ('withdrawal', 50.0)")
cursor.execute("INSERT INTO transactions (type, amount) VALUES ('deposit', 200.0)")


d = cursor.execute("SELECT * FROM TRANSACTIONS")
print(d.fetchall())

conexion.commit()
conexion.close()