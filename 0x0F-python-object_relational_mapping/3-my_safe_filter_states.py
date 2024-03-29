#!/usr/bin/python3
"""Script to get state by input"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], password=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER \
                BY states.id ASC", (argv[4], ))
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
