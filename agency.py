import sqlite3
import sys

(agency_name, borough) = sys.argv[1:3]

con.sqlite3.connect('nyc.db')
cur = con.cursor()

cur.execute("INSERT INTO AGENCY(agency_name, borough) VALUES(?,?)", [agency_name, borough])

con.commit()
cur.close()
