from hw09_upc_start import *
import sys

from inspect import getframeinfo, stack

def unittest(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: a boolean representing the test
    :return: None
    """

    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def hw09_test_suite():
    # We have began your test suite here. You should add more as you develop fruitful functions!
    unittest(is_valid_input("036000291452") == True)
    unittest(is_valid_input("1") == False)
    unittest(is_valid_modulo("123456789012") == 2)
    unittest(translate("123456789012")[0] == "101")


if __name__ == "__main__":
    hw09_test_suite()
