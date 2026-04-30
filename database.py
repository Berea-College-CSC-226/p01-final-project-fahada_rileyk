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


def insert_product(self, upc: str, name: str, quantity: int) -> bool:
    """
    Insert a new product into the database.

    Args:
        upc (str): UPC code (must be unique)
        name (str): Product name
        quantity (int): Initial quantity

    Returns:
        bool: True if successful, False if UPC already exists
    """
    try:
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO products (upc, name, quantity) VALUES (?, ?, ?)",
            (upc, name, quantity)
        )
        self.connection.commit()

        # Log initial inventory as a transaction
        self.log_transaction(upc, quantity)

        return True
    except sqlite3.IntegrityError:
        # UPC already exists (primary key violation)
        return False


def get_product(self, upc: str) -> Optional[Tuple[str, str, int]]:
    """
    Retrieve a product by UPC code.

    Args:
        upc (str): UPC code to search for

    Returns:
        tuple: (upc, name, quantity) if found, None otherwise
    """
    cursor = self.connection.cursor()
    cursor.execute(
        "SELECT upc, name, quantity FROM products WHERE upc = ?",
        (upc,)
    )
    result = cursor.fetchone()
    return result


def update_quantity(self, upc: str, new_quantity: int) -> bool:
    """
    Update the quantity of an existing product.

    Args:
        upc (str): UPC code of product to update
        new_quantity (int): New quantity value

    Returns:
        bool: True if successful, False if product not found
    """
    cursor = self.connection.cursor()
    cursor.execute(
        "UPDATE products SET quantity = ? WHERE upc = ?",
        (new_quantity, upc)
    )
    self.connection.commit()

    # Check if any row was actually updated
    return cursor.rowcount > 0