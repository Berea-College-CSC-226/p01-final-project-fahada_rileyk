######################################################################
# Author: A M Fahad
# Username: fahada
#
# Assignment: HW09: UPC Barcodes
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


def is_valid_input(barcode):

    "Returns if barcode is 12 digits and from 0-9. Or else should fail"

    return barcode.isdigit() and len(barcode) == 12

def get_valid_input():
    while True:
        barcode = input("Please enter a valid 12-digit barcode: ")
        if is_valid_input(barcode):
            return barcode

def is_valid_modulo(barcode):

    '''
    now I need to store all the strings of the input into a list as integers
    and I need to iterate through the odds and evens and do the appropriate
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

def translate(barcode_num):

    def invert(pattern):
        """
        Taking a binary string and flips each bit:
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
        result.append(invert(L_CODE[i]))

    result.append("101")  #adding the end guard

    return result

import turtle


def draw_barcode(barcode_num):
    patterns = translate(barcode_num)
    full_code = "".join(patterns)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()

    BAR_WIDTH = 5
    BAR_HEIGHT = 100

    # Center the barcode on screen
    total_width = len(full_code) * BAR_WIDTH
    t.goto(-total_width / 2, -50)

    for bit in full_code:
        x, y = t.pos()
        if bit == '1':
            t.pensize(BAR_WIDTH)
            t.pendown()
            t.setheading(90)
            t.forward(BAR_HEIGHT)
            t.penup()
            t.goto(x + BAR_WIDTH, y)
        else:
            t.goto(x + BAR_WIDTH, y)

    turtle.done()


def main():
    input_code = get_valid_input()

    if is_valid_modulo(input_code) == int(input_code[-1]):
        draw_barcode(input_code)
    else:
        print("Invalid barcode")

if __name__ == "__main__":
    main()
