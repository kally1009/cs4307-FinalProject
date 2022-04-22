import sqlite3
from sqlite3 import Error
import sys


corruption = 'SELECT avg(p.real_salary), a.location, h.avg_rent  FROM PEOPLE p JOIN AGENCY a on p.agency_id=a.id JOIN HOUSING h ON a.location=h.burrow'


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
