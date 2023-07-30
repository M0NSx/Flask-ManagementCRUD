import sqlite3 as sql

con = sql.connect('database3.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS products')
