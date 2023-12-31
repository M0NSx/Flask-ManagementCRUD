import sqlite3 as sql

con = sql.connect('database2.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS giveaways")

sql = """CREATE TABLE "giveaways"(

    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "GiveAwayName" Text,
    "Type" Text,
    "Reward" Text,
    "Entries" Text,
    "MaxWinners" Text,
    "InitialDate" Text,
    "Duration" Text

)"""

cur.execute(sql)
con.commit()
con.close()
