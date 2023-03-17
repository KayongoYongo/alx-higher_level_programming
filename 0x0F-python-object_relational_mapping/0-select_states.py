#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa. """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id ASC")
    for i in c.fetchall():
        print(i)

    c.close()
    db.close()
