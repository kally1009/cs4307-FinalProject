import sqlite3
from sqlite3 import Error
import sys


corruption = ' select id, f_name, last_name, (real_salary-base_salary) as salary_over_base FROM PEOPLE p JOIN JOBS j on p.job_title=j.job_title order by (real_salary-base_salary) desc limit count(id)/10'


def main():
    database = r"nyc.db"
    conn = sqlite3.connect(database)
    if conn is not None:
        try:
            c = conn.cursor()
            c.execute(corruption)
        except Error as e:
            print(e)
    else:
        print("Error! Cannot create the database connection.")


if __name__ == '__main__':
    main()
