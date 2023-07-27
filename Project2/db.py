import sqlite3 as sql

con = sql.connect('database2.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS giveaways")

sql = """CREATE TABLE "giveaways"(

    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "GiveAway Name" Text,
