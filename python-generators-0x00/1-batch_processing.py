#!/usr/bin/env python3
"""
Module to stream and process user data in batches using MySQL
"""
from seed import connect_to_prodev


def stream_users_in_batches(batch_size):
    """
    Generator function that yields batches of users from the MySQL database.
    
    Args:
        batch_size (int): Number of users to fetch in each batch
        
    Yields:
        list: A batch of users as dictionaries
    """
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    
    try:
        offset = 0
        while True:
            query = f"SELECT user_id, name, email, age FROM user_data LIMIT {batch_size} OFFSET {offset}"
            cursor.execute(query)
            batch = cursor.fetchall()
            
            if not batch:
                break
            
            yield batch
            offset += batch_size
    
    finally:
        cursor.close()
        connection.close()


def batch_processing(batch_size):
    """
    Process users in batches and print users older than 25.
    
    Args:
        batch_size (int): Size of each batch to process
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)


if __name__ == "__main__":
    # Example usage
    batch_processing(50)