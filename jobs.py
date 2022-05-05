import sqlite3
from ssl import ALERT_DESCRIPTION_UNRECOGNIZED_NAME
import sys

title = ''
agency = ''
string = sys.argv[1:]
for i in range(len(string)):
    if string[i] == 'OFFICE':
        title_name = string[1:i]
        agency_name = string[i:len(string)-3]
        base_salary = string[len(string)-2]
        location = string[len(string)-1]

        agency = ""
        for a in agency_name:
            agency += a
            agency += " "
        agency[1:len(agency)-1]

        title = ""
        for t in title_name:
            title += t
            title += " "
        title[1:len(title)-1]
        break

con = sqlite3.connect('nyc.db')
cur = con.cursor()
# load into interactive shell and lookup sqlite3 python and see the options there are.
# might be an iterator or tuple also check if it's query, etc.
cur.execute(
    "SELECT id FROM AGENCIES WHERE agency_name = ? AND borough=?", [agency, location])
agency_id = cur.fetchone()
if agency_id is None:
    cur.execute("INSERT INTO JOBS(job_title, agency_id, base_salary) VALUES(?,?,?)", [
                title, agency_id, base_salary])

con.commit()
cur.close()
