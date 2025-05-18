#!/usr/bin/env python3
"""
Generator Script to stream rows from MySQL database one by one
"""
from mysql.connector import Error
from seed import connect_to_prodev


def stream_data(connection, batch_size=10):
    """
    Generator function that streams data from the database one row at a time
    
    Args:
        connection: MySQL database connection
        batch_size: Number of records to fetch at once (for efficiency)
        
    Yields:
        Dictionary containing user data for each row
    """
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Get total number of records
        cursor.execute("SELECT COUNT(*) as count FROM user_data")
        total_records = cursor.fetchone()['count']
        print(f"Total records in database: {total_records}")
        
        # Stream records in batches for efficiency
        offset = 0
        while offset < total_records:
            query = f"""
                SELECT user_id, name, email, age 
                FROM user_data 
                LIMIT {batch_size} OFFSET {offset}
            """
            cursor.execute(query)
            
            # Yield one row at a time
            batch = cursor.fetchall()
            if not batch:
                break
                
            for row in batch:
                yield row
            
            offset += batch_size
            
        cursor.close()
        
    except Error as e:
        print(f"Error streaming data: {e}")
        yield None


def main():
    """Main function to demonstrate the generator usage"""
    # Connect to database
    connection = connect_to_prodev()
    if connection is None:
        return
    
    try:
        # Stream data using generator
        print("Streaming data from database:")
        print("-" * 50)
        
        for i, record in enumerate(stream_data(connection)):
            if record:
                print(f"Record {i+1}:")
                print(f"  User ID: {record['user_id']}")
                print(f"  Name: {record['name']}")
                print(f"  Email: {record['email']}")
                print(f"  Age: {record['age']}")
                print("-" * 50)
    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed")


if __name__ == "__main__":
    main()