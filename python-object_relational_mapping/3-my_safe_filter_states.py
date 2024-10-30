#!/usr/bin/python3
"""Takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument and
that is safe from MySQL injections"""

import sys
import MySQLdb

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    cursor.execute(query, (state_name,))

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
