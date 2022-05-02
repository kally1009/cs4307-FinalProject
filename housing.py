import sqlite3
import sys


con = sqlite3.connect('nyc.db')
cur = con.cursor()

cur.execute(
    "INSERT INTO HOUSING(borough, avg_rent, avg_buy, bedrooms) VALUES('MANHATTAN', 3785, 1290000, 1)")
cur.execute(
    "INSERT INTO HOUSING(borough, avg_rent, avg_buy, bedrooms) VALUES('BROOKLYN', 3350, 969000, 1)")
cur.execute(
    "INSERT INTO HOUSING(borough, avg_rent, avg_buy, bedrooms) VALUES('QUEENS', 2242, 699000, 1)")
cur.execute(
    "INSERT INTO HOUSING(borough, avg_rent, avg_buy, bedrooms) VALUES('STATEN ISLAND', 1500, 579908, 1)")
cur.execute(
    "INSERT INTO HOUSING(borough, avg_rent, avg_buy, bedrooms) VALUES('BRONX', 1800, 550000, 1)")

con.commit()
cur.close()
