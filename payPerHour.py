import sqlite3
from sqlite3 import Error
import sys

# Find ppl with the highest salary per hour worked
ezMoney = 'SELECT f_name, last_name, job_title, a.agency_name, (p.real_salary/p.hours) as salary_per_hour, p.real_salary as yearly_salary, p.hours FROM PEOPLE p JOIN JOBS j on p.job_title=j.job_title JOIN AGENCIES a on p.agency_id=a.id GROUP BY p.id ORDER BY salary_per_hour desc LIMIT 40'


def main():
    database = r"nyc.db"
    conn = sqlite3.connect(database)
    if conn is not None:
        try:
            c = conn.cursor()
            c.execute(ezMoney)
        except Error as e:
            print(e)
    else:
        print("Error! Cannot create the database connection.")


if __name__ == '__main__':
    main()
