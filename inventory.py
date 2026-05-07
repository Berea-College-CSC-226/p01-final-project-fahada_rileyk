######################################################################
# Author: A M Fahad, Boone B. Riley
# Username: fahada, rileyk
#
# Assignment: Final Project
#
# Purpose: Connects the database to the inventory
#
######################################################################
# Acknowledgements: StackOverflow, Youtube
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#####################################################################################

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
        # Validate name is not empty
        if not name or name.strip() == "":
            return False, "Product name cannot be empty."

        # Attempt to insert into database
        success = self.database.insert_product(upc, name, quantity)

        if success:
            return True, f"Product '{name}' added successfully with {quantity} units."
        else:
            return False, "Product with this UPC already exists."

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

    def stock_in(self, upc: str, quantity: int) -> Tuple[bool, str]:
        """
        Increase inventory (receive stock).

        Args:
            upc (str): UPC barcode
            quantity (int): Amount to add

        Returns:
            tuple: (success: bool, message: str)
        """
        # Validate UPC
        if not self.upc_validator.is_valid(upc):
            return False, "Invalid UPC code."

        # Validate quantity is positive
        if quantity <= 0:
            return False, "Stock in quantity must be positive."

        # Check if product exists
        product = self.database.get_product(upc)
        if not product:
            return False, "Product not found. Add it first."

        # Update inventory
        upc_code, name, current_quantity = product
        new_quantity = current_quantity + quantity

        self.database.update_quantity(upc, new_quantity)
        self.database.log_transaction(upc, quantity)

        return True, f"Stocked in {quantity} units. New quantity: {new_quantity}"

    def stock_out(self, upc: str, quantity: int) -> Tuple[bool, str]:
        """
        Decrease inventory (sell/remove stock).

        Prevents negative inventory.

        Args:
            upc (str): UPC barcode
            quantity (int): Amount to remove

        Returns:
            tuple: (success: bool, message: str)
        """
        # Validate UPC
        if not self.upc_validator.is_valid(upc):
            return False, "Invalid UPC code."

        # Validate quantity is positive
        if quantity <= 0:
            return False, "Stock out quantity must be positive."

        # Check if product exists
        product = self.database.get_product(upc)
        if not product:
            return False, "Product not found."

        # Check if sufficient stock available
        upc_code, name, current_quantity = product

        if current_quantity < quantity:
            return False, f"Insufficient stock. Available: {current_quantity}, Requested: {quantity}"

        # Update inventory
        new_quantity = current_quantity - quantity

        self.database.update_quantity(upc, new_quantity)
        self.database.log_transaction(upc, -quantity)  # Negative for stock out

        return True, f"Stocked out {quantity} units. New quantity: {new_quantity}"

    def get_all_products(self):
        """
        Get all products in inventory.

        Returns:
            list: All products as tuples (upc, name, quantity)
        """
        return self.database.get_all_products()

    def close(self):
        """Close database connection."""
        self.database.close()