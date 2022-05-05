import sqlite3
import sys
firstname, lastname, status, job_title, real_salary, hours, agency_name, borough = sys.argv[1:]

con = sqlite3.connect('nyc.db')
cur = con.cursor()

#print(agency_name, borough)
cur.execute("SELECT id FROM AGENCIES WHERE agency_name = ? AND borough = ?", [
            agency_name, borough])
result = cur.fetchone()
result = int(''.join(map(str, result)))
# print(result)

if result is not None:
    data = [firstname, lastname, status, job_title, real_salary, hours, result]
    cur.execute(
        "INSERT INTO PEOPLE(f_name, last_name, a_status, title, real_salary, hours_w, agency_id) VALUES(?,?,?,?,?,?,?)", data)
else:
    print("No agency ID :(", result)
    cur.execute("INSERT INTO PEOPLE(f_name, last_name, a_status, title, real_salary, hours_w, agency_id) VALUES(?,?,?,?,?,?,?)", [
                firstname, lastname, status, job_title, real_salary, hours, result])

con.commit()
cur.close()
