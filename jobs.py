import sqlite3
from ssl import ALERT_DESCRIPTION_UNRECOGNIZED_NAME
import sys

title, agency, salary, location = sys.argv[1:]
#print("title =", title, " agency= ", agency," salary= ", salary, location)

con = sqlite3.connect('nyc.db')
cur = con.cursor()
# load into interactive shell and lookup sqlite3 python and see the options there are.
# might be an iterator or tuple also check if it's query, etc.

cur.execute(
    "SELECT id FROM AGENCIES WHERE agency_name = ? AND borough=?", [agency, location])
agency_id = cur.fetchone()
agency_id = int(''.join(map(str, agency_id)))
# print(agency)
#print('agency_id=', agency_id)

if agency_id is not None:
    # print("yay")
    cur.execute(
        "SELECT * FROM JOBS WHERE job_title=? and agency_id=?", [title, agency_id])
    exists = cur.fetchone()
    if exists is None:
        cur.execute("INSERT INTO JOBS(job_title, agency_id, base_salary) VALUES(?,?,?)", [
                    title, agency_id, salary])
else:
    print("error- job already exists")

con.commit()
cur.close()
