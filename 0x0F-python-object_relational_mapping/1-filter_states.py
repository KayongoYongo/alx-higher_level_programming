#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa. """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         host="localhost", port=3306)
    c = db.cursor()
    """Three quotes have to be used in the query statement.
    Otherwise, the python interpreter will return an error,
    stating that it is an unterminated string literal"""
    """LIKE BINARY key word makes the comparison case
    sensitive"""
    c.execute("""SELECT * FROM states WHERE name
              LIKE BINARY 'N%' ORDER BY states.id ASC""")
    for i in c.fetchall():
        print(i)

    c.close()
    db.close()
