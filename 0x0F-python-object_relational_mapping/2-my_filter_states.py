#!/usr/bin/python3
""" Script that takes in an argument and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Grab the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
                        host="localhost",
                        user=username,
                        passwd=password,
                        db=db_name,
                        port=3306)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Construct the SQL query using the user input
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        state_name)

    # Execute the query
    cursor.execute(query)

    # Fetch all the rows and display them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
