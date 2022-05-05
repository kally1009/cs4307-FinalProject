import sqlite3
import sys

agency_name, borough = sys.argv[1:]

con = sqlite3.connect('nyc.db')
cur = con.cursor()

combo = [agency_name, borough]
cur.execute("SELECT id FROM AGENCIES WHERE agency_name=? AND borough=?", combo)
result = cur.fetchone()
print(result)
if result is None:
    print("yay")
    cur.execute("INSERT INTO AGENCIES (agency_name, borough) VALUES(?,?)", [agency_name, borough])
con.commit()
cur.close()
