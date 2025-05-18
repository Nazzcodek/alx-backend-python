#!/usr/bin/env python3
"""
Module to calculate the average age of users using generators
for memory efficiency with MySQL database
"""
from mysql.connector import Error
from seed import connect_to_prodev


def stream_user_ages():
    """
    Generator function that yields user ages one by one from MySQL.
    
    Yields:
        int: Age of a single user
    """
    connection = connect_to_prodev()
    cursor = connection.cursor()
    
    try:
        offset = 0
        batch_size = 100  # Process in small batches for efficiency
        
        while True:
            query = f"SELECT age FROM user_data LIMIT {batch_size} OFFSET {offset}"
            cursor.execute(query)
            batch = cursor.fetchall()
            
            if not batch:
                break
                
            for (age,) in batch:
                yield age
                
            offset += batch_size
    
    except Error as e:
        print(f"Database error: {e}")
    finally:
        cursor.close()
        connection.close()


def calculate_average_age():
    """
    Calculate the average age of users without loading all data into memory.
    
    Returns:
        float: The calculated average age
    """
    total_age = 0
    count = 0
    
    for age in stream_user_ages():
        total_age += age
        count += 1
    
    if count == 0:
        return 0
    
    return total_age / count


if __name__ == "__main__":
    avg_age = calculate_average_age()
    print(f"Average age of users: {avg_age:.2f}")