import sqlite3 as sql

con = sql.connect('database.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS users')

sql = """CREATE TABLE "users" (

    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "Name" TEXT,
    "Age" Text,
    "Street" Text,
    "City" Text,
    "Number" Text,
    "Email" Text

)"""

cur.execute(sql)
con.commit()
con.close()
