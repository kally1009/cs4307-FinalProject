import sqlite3
import sys
firstname, lastname, status, job_title, real_salary, hours, agency_name, borough = sys.argv[1:]

#job_title = f"'{job_title}'"
# agency_name = f"'{agency_name}'"
# borough = f"'{borough}'"


con = sqlite3.connect('nyc.db')
cur = con.cursor()

combo=(agency_name, borough)
print(agency_name, borough)
cur.execute("SELECT id FROM AGENCIES WHERE agency_name = ? AND borough = ?", combo)
result = cur.fetchone()
print(result)

""" if result is not None:
    data= [firstname, lastname, status, job_title, real_salary, hours, result]
    print("agency_id is", result)
    cur.execute("INSERT INTO PEOPLE(f_name, last_name, a_status, title, real_salary, hours_w, agency_id) VALUES(?,?,?,?,?,?,?)", data)
else:
    print("No agency ID, is None", result)
    cur.execute("INSERT INTO PEOPLE(f_name, last_name, a_status, title, real_salary, hours_w, agency_id) VALUES(?,?,?,?,?,?,?)", [firstname, lastname, status, job_title, real_salary, hours, result])
 """

con.commit()
cur.close()

