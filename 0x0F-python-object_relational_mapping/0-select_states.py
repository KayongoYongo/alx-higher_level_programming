#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id ASC")
    results = c.fetchall()

    for i in results:
        print(i)

    c.close()
    db.close()
