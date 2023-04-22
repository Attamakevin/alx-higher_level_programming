#!/usr/bin/python3
""" List all state in database """

import MySQLdb
import sys

if __name__ == '__main__':

    # Get MySQL username, password, and database name as command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server running on localhost at port 3306
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=username,
                           passwd=password,
                           db=database)

    # Create cursor to execute SQL queries
    cursor = conn.cursor()

    # Execute SQL query to retrieve all states from the database
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows returned by the query
    for row in cursor.fetchall():
        print(row)
