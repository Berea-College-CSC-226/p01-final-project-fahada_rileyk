from original_code.upc import UPC
from database import Database
from typing import Optional, Tuple

class InventoryManager:

    def __init__(self, db_path = "inventory.db"):

        """Initializes the inventory manager

        Arguments: db_path(str): this is the directory to the database file
        """

        self.upc_validator = UPC()
        self.database = Database(db_path) #Haven't worked on the Database file yet.



    def add_product(self, upc: str, name: str, quantity: int):

        if not self.upc_validator.is_valid(upc):
            return False, "Invalid UPC code. Check the format and checksum."
        if quantity < 0:
            return False, "Quantity cannot be negative."

    def search_product(self, upc: str) -> Tuple[bool, str, Optional[Tuple]]:
        """
        Search for a product by UPC.

        Args:
            upc (str): UPC barcode to search

        Returns:
            tuple: (success: bool, message: str, product_data: tuple or None)
        """
        # Validate UPC format
        if not self.upc_validator.is_valid(upc):
            return False, "Invalid UPC code.", None

        # Query database
        product = self.database.get_product(upc)

        if product:
            upc_code, name, quantity = product
            message = f"Product: {name}\nUPC: {upc_code}\nQuantity: {quantity}"
            return True, message, product
        else:
            return False, "Product not found.", None

    def close(self):
        """Close database connection."""
        self.database.close()