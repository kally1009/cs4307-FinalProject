import sqlite3
import sys

positionsBySalary = 'SELECT p.title, avg(p.real_salary) as avg_salary  FROM PEOPLE p JOIN AGENCIES a on p.agency_id=a.id GROUP BY p.title ORDER BY avg_salary desc'

con = sqlite3.connect('nyc.db')
cur = con.cursor()
cur.execute(positionsBySalary)
con.commit()
cur.close()

'
