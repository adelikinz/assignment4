import mysql.connector
from config import USER, PASSWORD, HOST


# Database connection exception
class DbConnectionError(Exception):
    pass


# Connect to the database
def _connect_to_db(db_name):
    try:
        cnx = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            auth_plugin='mysql_native_password',
            database=db_name
        )
        print("Successfully connected to the database:", db_name)
        return cnx
    except mysql.connector.Error as err:
        print("Error:", err)
        raise DbConnectionError("Failed to connect to the database")


# Select all pets from database
def db_pethaven_overview():
    db_connection = None
    cur = None
    try:
        db_name = "pethaven_db"  # the database name
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        # Selecting all the data from pets
        query = "SELECT * FROM pets"
        cur.execute(query)
        pets = cur.fetchall()
        return pets

    except mysql.connector.Error as err:
        print("Error:", err)
        return None

    finally:
        if cur:
            cur.close()
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# Select a specific pet by its id from the database
def db_pet_id(pet_id):
    db_connection = None
    cur = None
    try:
        db_name = "pethaven_db"  # the database name
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        # selecting a specific pet based on it's id
        query = """
        SELECT * FROM pets 
        WHERE pet_id = '{}';
        """.format(pet_id)

        cur.execute(query)
        pets = cur.fetchall()

        # Extract the pet's information into a list
        pet = [pet for pet in pets[0]]
        return pet

    except mysql.connector.Error as err:
        print("Error:", err)
        return None

    finally:
        if cur:
            cur.close()
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


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


