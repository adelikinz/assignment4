import mysql.connector
from config import HOST, USER, PASSWORD

class DbConnectionError(Exception):
    pass

# every function should be in a try/catch statement as we are connecting to database here


def _connect_to_db(db_name):
# establish connection to database using config file


def find_customer_db(query, values):
# database call that searches for customer id by existing customer name and email.


def create_customer_db(query):
# creates customer in the database with the user-input customer name and email, this also returns customer id to be used elsewhere.

def db_call_without_values(query):
    availability = []
    try:
        db_name = 'pethaven_db'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        cur.execute(query)

        result = cur.fetchall()
        availability = result
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return availability
# general database call that executes a sql query and returns the results and assigns it to the variable 'availability'.


def db_call_with_values_without_return(query, values):
    try:
        db_name = 'pethaven_db'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        print("Executing query:", query)
        cur.execute(query, values)
        db_connection.commit()
        cur.close()

    except Exception as e:
        print("Error:", e)
        raise DbConnectionError("db_call_with_values_without_return failed")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
# this function is a reusable db call that takes a sql query with values(user input) and commits the values into database


def db_call_with_values(query, values):
    items = []
    try:
        db_name = 'pethaven_db'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        cur.execute(query, values)

        result = cur.fetchall()
        items = result
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return items
# this function is a reusable db call that takes and executes a sql query with the value(user input)
# and returns results as the variable 'items'

