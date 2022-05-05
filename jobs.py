import sqlite3
import sys

(job_title, base_salary, agency_name) = sys.argv[1:3]
print('\n job title=', job_title, "agency_name=", agency_name, "base_salary=", base_salary)

con = sqlite3.connect('nyc.db')
cur = con.cursor()
# load into interactive shell and lookup sqlite3 python and see the options there are.
# might be an iterator or tuple also check if it's query, etc.
agency_id = cur.execute(
    "SELECT id FROM AGENCIES WHERE agency_name = ? ", agency_name)
cur.execute("INSERT INTO JOBS(job_title, agency_id, base_salary) VALUES(?,?,?)", [
            job_title, agency_id, base_salary])

con.commit()
cur.close()
