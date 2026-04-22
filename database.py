import sqlite3

class Database:

    def __init__(self, db_path = "inventory.db"):

        """Initializing database connection and creating some tables if it's
        necessary."""
        self.db_path = db_path
        self.connection = None
        self.initialize_database()

    def initialize_database(self):
        """Sqlite3 code that aims to connect the database"""
        self.connection = sqlite3.connect(self.db_path)
        cursor = self.connection.cursor()

        # Create products table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                upc TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL DEFAULT 0
            )
        """)

        # Create transactions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                upc TEXT NOT NULL,
                change INTEGER NOT NULL,
                timestamp TEXT NOT NULL,
                FOREIGN KEY (upc) REFERENCES products(upc)
            )
        """)

        self.connection.commit()
