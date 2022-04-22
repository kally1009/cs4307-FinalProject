import sqlite3
import sys

(first_name, last_name, status, job_title, salary, hours, agency) = sys.argv[1:8]

con = sqlite3.connect('nyc.db')
cur = con.cursor()

cur.execute("INSERT INTO PEOPLE(f_name, last_name, status, job_title, real_salary, hours, agency_id) VALUES(?,?,?,?,?,?,?)", [
    first_name, last_name, status, job_title, salary, hours, agency])

con.commit()
cur.close()

