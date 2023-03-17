#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa. """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         host="localhost", port=3306)
    c = db.cursor()

    """Preparing SQL statements"""
    selectQuery = "SELECT * FROM states WHERE name LIKE %s "
    queryParameter = (sys.argv[4],)

    """Executing th SQL query with parameterized values
    to prevent SQL injection"""
    c.execute(selectQuery, queryParameter)

    for i in c.fetchall():
        print(i)

    c.close()
    db.close()
