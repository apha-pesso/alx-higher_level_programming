#!/usr/bin/python3
"""Get all cities by state"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], password=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
                JOIN states ON cities.state_id=states.id \
                WHERE states.name LIKE %s", (argv[4], ))

    lamb = []
    for city in cur.fetchall():
        lamb.append(city[0])
    print(", ".join(lamb))
    cur.close()
    db.close()
