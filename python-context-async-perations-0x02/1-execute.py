import sqlite3

class ExecuteQuery:
    """A context manager class for executing database queries"""
    
    def __init__(self, database_name, query, parameters=None):
        """Initialize with database name, query, and optional parameters"""
        self.database_name = database_name
        self.query = query
        self.parameters = parameters or ()
        self.connection = None
        self.cursor = None
        self.results = None
    
    def __enter__(self):
        """Enter the context - open connection and execute query"""
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.parameters)
        self.results = self.cursor.fetchall()
        return self.results
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the context - close cursor and connection"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        # Return False to propagate any exceptions
        return False

# Using the ExecuteQuery context manager
with ExecuteQuery('users.db', "SELECT * FROM users WHERE age > ?", (25,)) as results:
    print("Users older than 25:")
    for user in results:
        print(user)