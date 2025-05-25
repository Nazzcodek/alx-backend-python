import sqlite3

class DatabaseConnection:
    """A context manager class for handling database connections"""
    
    def __init__(self, database_name):
        """Initialize with database name"""
        self.database_name = database_name
        self.connection = None
    
    def __enter__(self):
        """Enter the context - open database connection"""
        self.connection = sqlite3.connect(self.database_name)
        return self.connection
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the context - close database connection"""
        if self.connection:
            self.connection.close()
        # Return False to propagate any exceptions
        return False

# Using the context manager to perform a query
with DatabaseConnection('users.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    
    print("Users from database:")
    for user in results:
        print(user)