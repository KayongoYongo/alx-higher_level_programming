#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa. """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         host="localhost", port=3306)
    c = db.cursor()

    """Preparing SQL statements"""
    selectQuery = """SELECT cities.name FROM
                  cities INNER JOIN states ON states.id=cities.state_id
                  WHERE states.name LIKE %s"""
    queryParameter = (sys.argv[4],)

    """Executing th SQL query with parameterized values
    to prevent SQL injection"""
    c.execute(selectQuery, queryParameter)

    rows = c.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")

    c.close()
    db.close()
