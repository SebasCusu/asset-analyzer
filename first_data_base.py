import sqlite3

conexion = sqlite3.connect("mi_base.db")
cursor = conexion.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)"
)

cursor.execute("INSERT INTO users (name, age) VALUES ('John', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Luke', 15)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Mathew', 14)")

conexion.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conexion.close()
