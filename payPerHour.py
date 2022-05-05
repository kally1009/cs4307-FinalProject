import sqlite3
from sqlite3 import Error
import sys

# Find ppl with the highest salary per hour worked
ezMoney = 'SELECT f_name, last_name, (p.real_salary/p.hours_w) as salary_per_hour, p.real_salary as yearly_salary, p.hours_w FROM PEOPLE p JOIN JOBS j on p.title=j.job_title JOIN AGENCIES a on p.agency_id=a.id GROUP BY p.id ORDER BY salary_per_hour desc LIMIT 40'


def main():
    database = "nyc.db"
    conn = sqlite3.connect(database)
    if conn is not None:
        try:
            c = conn.cursor()
            c.execute(ezMoney)
            result = c.fetchall()
            print("Pay per Hour")
            print(result)
        except Error as e:
            print(e)
    else:
        print("Error! Cannot create the database connection.")


if __name__ == '__main__':
    main()
