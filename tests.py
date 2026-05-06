######################################################################
# Author: A M Fahad, Boone B. Riley
# Username: fahada, rileyk
#
# Assignment: Final Project
#
# Purpose: Test Suite for the Final Project. Currently only contains UPC tests. Writing tests
# was tedious and this is something we need to improve on in our next project, to have a better
# suite, that would have saved a lot of time trying to debug our functions.
######################################################################
# Acknowledgements: StackOverflow, Youtube
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import unittest
from original_code.upc import UPC

class TestUPC(unittest.TestCase):

    def setUp(self):
        self.upc = UPC()

    #This section is testing the input validation of the UPC classes code

    def test_valid_upc_input(self):
        self.assertTrue(self.upc.is_valid_input("036000291452"))

    def test_invalid_length_short(self):
        self.assertFalse(self.upc.is_valid_input("123456789"))

    def test_invalid_length_long(self):
        self.assertFalse(self.upc.is_valid_input("1234567890123"))

    def test_invalid_characters(self):
        self.assertFalse(self.upc.is_valid_input("12345A789012"))


    def test_modulo_valid_upc(self):
        upc = "036000291452"
        self.assertEqual(
            self.upc.is_valid_modulo(upc),
            int(upc[-1])
        )

    def test_modulo_invalid_length(self):
        self.assertEqual(
            self.upc.is_valid_modulo("123"),
            -1
        )

    "This Section is going to test the invert logic for the UPC"


    def test_invert_basic(self):
        self.assertEqual(self.upc.invert("0101"), "1010")

    def test_invert_all_zeros(self):
        self.assertEqual(self.upc.invert("0000"), "1111")

    def test_invert_all_ones(self):
        self.assertEqual(self.upc.invert("1111"), "0000")

    #This is testing if the translation does contain the guard bars and that they're working

    def test_translate_contains_guard_bars(self):
        result = self.upc.translate("036000291452", None)
        self.assertEqual(result[0], "101")
        self.assertEqual(result[7], "01010")
        self.assertEqual(result[-1], "101")




if __name__ == "__main__":
    unittest.main()