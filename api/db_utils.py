import mysql.connector
from config import HOST, USER, PASSWORD

class DbConnectionError(Exception):
    pass

# every function should be in a try/catch statement as we are connecting to database here

def _connect_to_db(db_name):
    # establish connection to database using config file
    db_connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=db_name
    )
    return db_connection
# establish connection to database using config file


def find_customer_db(query, values):
    # database call that searches for customer id by existing customer name and email.
    pass

def create_customer_db(query):
    # creates customer in the database with the user-input customer name and email, this also returns customer id to be used elsewhere.
    pass

def db_call_without_values(query):
    # general database call that executes query but doesn't return anything.
    pass

def db_call_with_values_without_return(query, values):
    # general db call that takes values and does not return anything
    pass


def db_call_with_values(query, values):
    # general db call that takes query with values and returns results
    pass


# Add booking to the SQL database
def add_booking_to_db(pet_id, customer_id, timeslot, booking_date):
    try:
        # Connect to the database
        db_name = 'pethaven_db'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to Database")

        # the SQL query for updating the pet bookings
        query = """
        UPDATE pet_bookings
        SET pet_id = {}, timeslot_{} = {}, booking_id_{} = {}
        WHERE bookingDate = '{}';
        """.format(pet_id, timeslot, customer_id, timeslot, customer_id, booking_date)

        # Executes the query and then commits
        cur.execute(query)
        db_connection.commit()

        cur.close()

        # returns the booking details
        return {'pet_id': pet_id, 'customer_id': customer_id, 'timeslot': timeslot, 'booking_date': booking_date}

    except Exception as e:
        raise DbConnectionError("Failed to read data in Database") from e

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def cancel_bookings(pet_id):
    try:
        db_name = 'pethaven_db'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()

        # Cancel existing bookings for the pet
        query = """
        UPDATE pet_bookings
        SET booking_id_9_11 = NULL, booking_id_13_15 = NULL, booking_id_17_19 = NULL
        WHERE pet_id = %s
        """
        cur.execute(query, (pet_id,))
        db_connection.commit()

        cur.close()

    except mysql.connector.Error as e:
        raise DbConnectionError("Failed cancellation of existing bookings") from e

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

def update_pet_availability(pet_id):
    try:
        db_name = 'pethaven_db'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()

        # Update pet availability to not available for rent
        query = """
        UPDATE pets
        SET available_for_rent = 0
        WHERE pet_id = %s
        """
        cur.execute(query, (pet_id,))
        db_connection.commit()

        cur.close()

    except mysql.connector.Error as e:
        raise DbConnectionError("Update failure for pet availability") from e

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")