#!/usr/bin/env python3
"""
Module to lazily paginate user data from MySQL
"""
from mysql.connector import Error
from seed import connect_to_prodev


def paginate_users(page_size, offset):
    """
    Fetch a page of users from the database.
    
    Args:
        page_size (int): Number of users to fetch in a page
        offset (int): Starting position for fetching users
        
    Returns:
        list: A page of users as dictionaries
    """
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    
    try:
        query = f"SELECT user_id, name, email, age FROM user_data LIMIT {page_size} OFFSET {offset}"
        cursor.execute(query)
        return cursor.fetchall()
    except Error as e:
        print(f"Error fetching data: {e}")
        return []
    finally:
        cursor.close()
        connection.close()


def lazy_pagination(page_size):
    """
    Generator function that yields pages of user data as needed.
    
    Args:
        page_size (int): Size of each page to fetch
        
    Yields:
        list: A page of users as dictionaries
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size


if __name__ == "__main__":
    lazy_pagination()