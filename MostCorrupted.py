import sqlite3
from sqlite3 import Error
import sys


corruption = 'SELECT id, f_name, last_name, job_title, (j.base_salary-p.real_salary) as salary_over_base FROM PEOPLE p JOIN JOBS j on p.title=j.job_title ORDER BY (p.real_salary-j.base_salary) desc'


def main():
    database = r"nyc.db"
    conn = sqlite3.connect(database)
    if conn is not None:
        try:
            c = conn.cursor()
            c.execute(corruption)
            result = c.fetchall()
            print("Most Corrupted", result)
        except Error as e:
            print(e)
    else:
        print("Error! Cannot create the database connection.")


if __name__ == '__main__':
    main()
