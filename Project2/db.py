import sqlite3 as sql

con = sql.connect('database2.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS giveaways")
