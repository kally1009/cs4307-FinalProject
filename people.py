import sqlite3
import sys

(first_name, last_name, status, job_title, salary, hours, agency) = sys.argv[1:8]

con = sqlite3.connect('nyc.db')
cur = con.cursor()

agency_id = cur.execute("SELECT id FROM AGENCIES WHERE agency_name = ?", agency)
title = cur.execute("SELECT job_title FROM JOBS WHERE job_title = ? AND agency_id = ?", job_title, agency_id)


cur.execute("INSERT INTO PEOPLE(f_name, last_name, status, job_title, real_salary, hours, agency_id) VALUES(?,?,?,?,?,?,?)", [
    first_name, last_name, status, title, salary, hours, agency_id])

con.commit()
cur.close()

