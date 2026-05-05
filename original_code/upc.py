######################################################################
# Author: A M Fahad
# Username: fahada
#
# Assignment: Berea Quad Walmart - Inventory Management System
# UPC Validation Module (adapted from HW09)
#
# Purpose: Validate UPC barcodes for inventory system
#
######################################################################
# Acknowledgements:
# Original UPC validation logic from HW09
# Adapted for inventory management system use
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################


class UPC:
    """
    UPC barcode validator.
    Validates 12-digit UPC codes using modulo checksum algorithm.
    """

    def __init__(self):
        """Initialize UPC validator."""
        pass

    def is_valid_input(self, barcode):
        """
        Returns if barcode is 12 digits and from 0-9. Or else should fail.

        Args:
            barcode (str): The barcode string to validate

        Returns:
            bool: True if barcode is 12 digits and numeric, False otherwise
        """
        return barcode.isdigit() and len(barcode) == 12

    def is_valid_modulo(self, barcode):
        """
        Stores all the strings of the input into a list as integers
        and iterates through the odds and evens and does the appropriate
        modulo check for them.

        Args:
            barcode (str): The 12-digit barcode to validate

        Returns:
            int: The calculated check digit, or -1 if invalid length
        """
        if len(barcode) != 12:
            return -1

        digits = [int(d) for d in barcode]

        odd_sum = 0
        even_sum = 0
        for i in range(0, 11, 2):
            odd_sum = odd_sum + digits[i]
        for i in range(1, 11, 2):
            even_sum = even_sum + digits[i]

        total = (odd_sum * 3) + even_sum
        remainder = total % 10

        if remainder == 0:
            return 0
        else:
            return 10 - remainder

    def is_valid(self, barcode):
        """
        Complete validation: checks format and checksum.

        Args:
            barcode (str): The barcode to validate

        Returns:
            bool: True if barcode passes all validation, False otherwise
        """
        if not self.is_valid_input(barcode):
            return False

        calculated_check = self.is_valid_modulo(barcode)
        actual_check = int(barcode[-1])

        return calculated_check == actual_check
