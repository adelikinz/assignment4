import mysql.connector
from config import HOST, USER, PASSWORD

class DbConnectionError(Exception):
    pass

# every function should be in a try/catch statement as we are connecting to database here

def _connect_to_db(db_name):
# establish connection to database using config file


def db_call_without_values(query):
# general database call that executes query but doesn't return anything.


def find_customer_db(query, values):
# database call that searches for customer id by existing customer name and email.


def create_customer_db(query):
# creates customer in the database with the inputted customer name and email should also return customer id to be used elsewhere


def db_call_with_values_without_return(query, values):
# general db call that takes values and does not return anything


def db_call_with_values(query, values):
# general db call that takes query with values and returns results


