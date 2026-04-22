######################################################################
# Author: A M Fahad
# Username: fahada
#
# Assignment: HW09: UPC Barcodes with classes
#
# Purpose: Verify a barcode and draw it, if valid
#
######################################################################
# Acknowledgements:
#
# None: Original work

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle

class UPC:
    def __init__(self):
        self.BAR_WIDTH = 5
        self.BAR_HEIGHT = 100

    def is_valid_input(self, barcode):
        "Returns if barcode is 12 digits and from 0-9. Or else should fail"
        return barcode.isdigit() and len(barcode) == 12

    def is_valid_modulo(self, barcode):
        '''
        Stores all the strings of the input into a list as integers
        and iterates through the odds and evens and does the appropriate
        modulo check for them
        '''
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

    def invert(self, pattern):
        """
        Taking a binary string and flipping every bit:
        0 -> 1
        1 -> 0
        """
        inverted = ""
        for bit in pattern:
            if bit == '0':
                inverted += '1'
            else:
                inverted += '0'
        return inverted

    def translate(self, barcode_num, side):
        L_CODE = {
            '0': '0001101',
            '1': '0011001',
            '2': '0010011',
            '3': '0111101',
            '4': '0100011',
            '5': '0110001',
            '6': '0101111',
            '7': '0111011',
            '8': '0110111',
            '9': '0001011'
        }

        result = []

        result.append("101")  # start guard

        for i in barcode_num[0:6]:
            result.append(L_CODE[i])

        result.append("01010")  # middle guard

        for i in barcode_num[6:]:
            result.append(self.invert(L_CODE[i]))

        result.append("101")  # end guard

        return result

    def draw_barcode(self, barcode_num):
        patterns = self.translate(barcode_num, None)
        full_code = "".join(patterns)  # smashing everything from translate into one full barcode

        t = turtle.Turtle()
        t.speed(0)
        t.hideturtle()
        t.penup()

        # Centering the barcode on screen
        total_width = len(full_code) * self.BAR_WIDTH
        t.goto(-total_width / 2, -50)

        for bit in full_code:
            x, y = t.pos()  # saving the turtle position
            if bit == '1':
                t.pensize(self.BAR_WIDTH)
                t.pendown()
                t.setheading(90)
                t.forward(self.BAR_HEIGHT)
                t.penup()
                t.goto(x + self.BAR_WIDTH, y)
            else:
                t.goto(x + self.BAR_WIDTH, y)

        turtle.done()

    def draw_error(self):
        t = turtle.Turtle()
        t.speed(0)
        t.hideturtle()
        t.penup()
        t.goto(-100, 0)
        t.pendown()
        t.write("Invalid barcode!", font=("Arial", 24, "normal"))
        turtle.done()

        #Added a little drawing in case there's a bad barcode :P


def main():
    upc = UPC()

    input_code = input("Enter a 12 digit code [0-9]: ")
    while not upc.is_valid_input(input_code):
        input_code = input("Please enter a valid 12-digit barcode: ")

    if upc.is_valid_modulo(input_code) == int(input_code[-1]):
        upc.draw_barcode(input_code)
    else:
        upc.draw_error()

if __name__ == "__main__":
    main()
