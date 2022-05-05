import sqlite3
import sys


agency_name, borough = sys.argv[1:]

print("Job Title", agency_name)
print(borough)


con = sqlite3.connect('nyc.db')
cur = con.cursor()

cur.execute("SELECT agency_name, borough FROM AGENCIES WHERE agency_name=? AND borough=?", [agency_name, borough])
result = cur.fetchone()
if result is None:
    cur.execute("INSERT INTO AGENCIES (agency_name, borough) VALUES(?,?)", [agency_name,borough])

con.commit()
cur.close()
