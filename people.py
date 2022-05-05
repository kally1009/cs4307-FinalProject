import sqlite3
import sys
firstname, lastname, status, job_title, real_salary, hours, agency_name, borough = sys.argv[1:]

print('firstname ', firstname)
print('lastname ', lastname)
print('status ', status)

job_title = f"'{job_title}'"
print(job_title)
print('salary ', real_salary)

print('hours ', hours)

agency_name = f"'{agency_name}'"
print(agency_name)


con = sqlite3.connect('nyc.db')
cur = con.cursor()

agency = cur.execute("SELECT id FROM AGENCIES WHERE agency_name = ? AND borough = ?", [agency_name, borough])
#title = cur.execute("SELECT job_title FROM JOBS WHERE job_title = ? AND agency_id = ?", job_title, agency_id)
agency_id = cur.fetchone()
print("agency_id", agency_id)
#print("job_title", title)

cur.execute("INSERT INTO PEOPLE(f_name, last_name, a_status, title, real_salary, hours_w, agency_id) VALUES(?,?,?,?,?,?,?)", [firstname, lastname, status, job_title, real_salary, hours, agency_id])

con.commit()
cur.close()

