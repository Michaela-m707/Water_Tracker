import sqlite3
con = sqlite3.connect("watertracker.db")

cur = con.cursor()

res = cur.execute("SELECT * FROM water_intake")
print(res.fetchall())

