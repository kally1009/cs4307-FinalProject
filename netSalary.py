import sqlite3
from sqlite3 import Error
import sys


net_salary= 'SELECT a.agency_name, p.title,  a.borough, avg(p.real_salary)-h.avg_rent as avg_salary_after_rent  FROM PEOPLE p JOIN AGENCIES a on p.agency_id=a.id JOIN HOUSING h ON a.borough=h.borough'


def main():
    database = r"nyc.db"
    conn = sqlite3.connect(database)
    if conn is not None:
        try:
            c = conn.cursor()
            c.execute(net_salary)
        except Error as e:
            print(e)
    else:
        print("Error! Cannot create the database connection.")


if __name__ == '__main__':
    main()
