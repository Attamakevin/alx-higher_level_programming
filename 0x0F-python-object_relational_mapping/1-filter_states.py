#!/usr/bin/python3
"""a script that lists all states with a name starting with N (upper N) """

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY states.id ASC")
    rows = cursor.fetchall()

    for row in rows:
        if row[1][0] == 'N':
            print(row)
