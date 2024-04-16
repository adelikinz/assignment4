DROP DATABASE IF EXISTS pethaven_db;
CREATE DATABASE pethaven_db;
USE pethaven_db;

CREATE TABLE IF NOT EXISTS pets (
    pet_id INT AUTO_INCREMENT PRIMARY KEY,
    pet_name VARCHAR(100) NOT NULL,
    pet_type VARCHAR(50) NOT NULL,
    age INT,
    available_for_rent BOOLEAN DEFAULT 1
);

CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    customer_email VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS pet_bookings (
    pet_id INT,
    timeslot_9_11 INT DEFAULT NULL,
    booking_id_9_11 INT DEFAULT NULL,
    timeslot_13_15 INT DEFAULT NULL,
    booking_id_13_15 INT DEFAULT NULL,
    timeslot_17_19 INT DEFAULT NULL,
    booking_id_17_19 INT DEFAULT NULL,
    bookingDate DATE NOT NULL,
    FOREIGN KEY (pet_id) REFERENCES pets(pet_id),
    FOREIGN KEY (booking_id_9_11) REFERENCES customers(customer_id),
    FOREIGN KEY (booking_id_13_15) REFERENCES customers(customer_id),
    FOREIGN KEY (booking_id_17_19) REFERENCES customers(customer_id)
); 

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `filldates`(dateStart DATE, dateEnd DATE, pet_id INT)
BEGIN
  WHILE dateStart <= dateEnd DO
    INSERT INTO pet_bookings (pet_id, bookingDate) VALUES (pet_id, dateStart);
    SET dateStart = date_add(dateStart, INTERVAL 1 DAY);
  END WHILE;
END$$
DELIMITER ;

-- adding data to tables

-- existing data for the pets table
INSERT INTO pets (pet_name, pet_type, age, available_for_rent) VALUES 
('Buddy', 'Dog', 3, 1),
('Whiskers', 'Cat', 2, 1),
('Nibbles', 'Hamster', 1, 1);

-- existing data for the customers table
INSERT INTO customers (customer_name, customer_email) VALUES 
('john Doe', 'john@example.com'),
('alice Smith', 'alice@example.com'),
('bob Johnson', 'bob@example.com');

CALL `pethaven_db`.`filldates`(20240401, 20240407, 1);
CALL `pethaven_db`.`filldates`(20240401, 20240407, 2);
CALL `pethaven_db`.`filldates`(20240401, 20240407, 3);
