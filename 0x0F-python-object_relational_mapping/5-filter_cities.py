#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb as db


def connect_and_query() -> None:

    """Connect to the database and execute query"""
    try:
        cnx = db.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        cursor = cnx.cursor(cursorclass=db.cursors.Cursor)
        cursor.execute('SELECT city.name, state.name\
                        FROM cities as city\
                        INNER JOIN states as state\
                        ON city.state_id = state.id\
                        ORDER BY city.id ASC;')
        cities = cursor.fetchall()
        cities_list = []
        for city in cities:
            if city[1] == sys.argv[4]:
                cities_list.append(city[0])
        print(", ".join(list(dict.fromkeys((cities_list)))))

        cursor.close()
        cnx.close()
    except Exception as e:
        return (e)
