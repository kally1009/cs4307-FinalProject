import sqlite3
import sys


data = sys.argv[1:]

sData=data
borough=sData[len(sData)-1:]
title= "" 
for i in range(len(sData)-2):
    title += sData[i]
    title += " "
title = title[0:len(title)-1]

sData[0:len(sData)-1]

combo=borough
combo.append(title)

con = sqlite3.connect('nyc.db')
cur = con.cursor()

cur.execute("INSERT INTO AGENCIES (agency_name, borough) VALUES(?,?)", combo)

con.commit()
cur.close()
