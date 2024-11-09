from db import DB_PATH
import sqlite3
from sqlite3 import Error


def execute_query(query):
    connection = create_connection(DB_PATH)

    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
        return True
    except Error as e:
        print(f"The error '{e}' occurred")
        return False

def execute_read_query(query):
    connection = create_connection(DB_PATH)

    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")