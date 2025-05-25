import time
import sqlite3 
import functools

def with_db_connection(func):
    """Decorator that automatically handles database connection opening and closing"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Open database connection
        conn = sqlite3.connect('users.db')
        try:
            # Call the original function with connection as first argument
            result = func(conn, *args, **kwargs)
            return result
        finally:
            # Always close the connection, even if an exception occurs
            conn.close()
    
    return wrapper

query_cache = {}

def cache_query(func):
    """Decorator that caches query results based on the SQL query string"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract the query from arguments
        query = None
        if 'query' in kwargs:
            query = kwargs['query']
        elif len(args) > 1:  # Assuming query is the second argument after conn
            query = args[1]
        
        # Check if query result is already cached
        if query and query in query_cache:
            print(f"Cache hit for query: {query}")
            return query_cache[query]
        
        # Execute the function and cache the result
        result = func(*args, **kwargs)
        
        # Cache the result if we have a query
        if query:
            query_cache[query] = result
            print(f"Query cached: {query}")
        
        return result
    
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")