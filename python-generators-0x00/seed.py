#!/usr/bin/env python3
"""
Script to set up MySQL database and populate it with data from CSV
Creates ALX_prodev database with user_data table
"""
import mysql.connector
import csv
import uuid
import sys
from mysql.connector import Error


def connect_db():
    """Connects to the MySQL database server"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"  # Change these credentials as needed
        )
        print("MySQL Database connection successful")
        return connection
    except Error as e:
        print(f"Error connecting to MySQL Database: {e}")
        return None


def create_database(connection):
    """Creates the database ALX_prodev if it does not exist"""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created successfully")
    except Error as e:
        print(f"Error creating database: {e}")


def connect_to_prodev():
    """Connects to the ALX_prodev database in MySQL"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",  # Change these credentials as needed
            database="ALX_prodev"
        )
        print("Connected to ALX_prodev database")
        return connection
    except Error as e:
        print(f"Error connecting to ALX_prodev database: {e}")
        return None


def create_table(connection):
    """Creates a table user_data if it does not exist with required fields"""
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id VARCHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(5,2) NOT NULL,
                INDEX (user_id)
            )
        """)
        connection.commit()
        print("Table user_data created successfully")
    except Error as e:
        print(f"Error creating table: {e}")


def insert_data(connection, data):
    """
    Inserts data in the database if it does not exist
    
    Args:
        connection: MySQL database connection
        data: Dictionary containing user data
    """
    try:
        cursor = connection.cursor()
        
        # Check if the record with this user_id already exists
        check_query = "SELECT COUNT(*) FROM user_data WHERE user_id = %s"
        cursor.execute(check_query, (data['user_id'],))
        result = cursor.fetchone()
        
        # If record does not exist, insert it
        if result[0] == 0:
            insert_query = """
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_query, (
                data['user_id'],
                data['name'],
                data['email'],
                data['age']
            ))
            connection.commit()
            print(f"Record inserted for user: {data['name']}")
        else:
            print(f"Record already exists for user_id: {data['user_id']}")
    
    except Error as e:
        print(f"Error inserting data: {e}")


def load_data_from_csv(file_path):
    """
    Loads data from a CSV file
    
    Args:
        file_path: Path to the CSV file
        
    Returns:
        List of dictionaries containing user data
    """
    try:
        data = []
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Generate UUID for user_id if not present
                if 'user_id' not in row or not row['user_id']:
                    row['user_id'] = str(uuid.uuid4())
                data.append(row)
        return data
    except Exception as e:
        print(f"Error loading data from CSV: {e}")
        return []


def main():
    """Main function to execute the script"""
    # Connect to MySQL server
    connection = connect_db()
    if connection is None:
        return
    
    # Create database
    create_database(connection)
    connection.close()
    
    # Connect to ALX_prodev database
    prodev_connection = connect_to_prodev()
    if prodev_connection is None:
        return
    
    # Create table
    create_table(prodev_connection)
    
    # Load and insert data from CSV
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
    else:
        csv_file = "user_data.csv"
    
    try:
        user_data = load_data_from_csv(csv_file)
        for data in user_data:
            insert_data(prodev_connection, data)
        print(f"Successfully processed {len(user_data)} records")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if prodev_connection.is_connected():
            prodev_connection.close()
            print("MySQL connection closed")


if __name__ == "__main__":
    main()