from original_code.upc import UPC
from database import Database

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