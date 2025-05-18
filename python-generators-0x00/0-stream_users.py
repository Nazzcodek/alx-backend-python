#!/usr/bin/env python3
"""
Generator Script to stream rows from MySQL database one by one
"""
from mysql.connector import Error
from seed import connect_to_prodev


def stream_users():
    """
    Generator function that streams data from the database one row at a time
    
    Yields:
        Dictionary containing user data for each row
    """
    connection = connect_to_prodev()
    if connection is None:
        return
        
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Use a single query with no LIMIT to fetch all records
        cursor.execute("SELECT user_id, name, email, age FROM user_data")
        
        # Yield one row at a time as the cursor fetches them
        for row in cursor:
            yield row
            
    except Error as e:
        print(f"Error streaming data: {e}")
    finally:
        cursor.close()
        if connection.is_connected():
            connection.close()


if __name__ == "__main__":
    # Simple demonstration
    print("Streaming user data:")
    print("-" * 40)
    
    count = 0
    for user in stream_users():
        print(f"User: {user['name']}, Age: {user['age']}, Email: {user['email']}")
        count += 1
        if count >= 5:  # Just show first 5 users for demo
            print("...")
            break
            
    print(f"\nSuccessfully streamed data for {count} users")