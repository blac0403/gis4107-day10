#-------------------------------------------------------------------------------
# Name:        Module name
# Purpose:     Brief desciption of what module does
# Usage:       Module name and required/optional command-line parameters (if any)
# Author:      Your name(s)
#
# Created:     Date
#-------------------------------------------------------------------------------
import os
import sys

_fmtPassed = "Passed: {}"
_fmtFailed = "Failed: {}\n  Expect: {}\n  Actual: {}"
_scriptFolder = os.path.dirname(os.path.abspath(__file__))

def main():
    test_func1()

def func1(params):
    """Function documentation:
       - What does function do?
       - What is/are expected parameter value(s)?
       - What does function return, if anything
       - Example usage"""
    pass

def test_func1():
    # Test case 1
    expected = "expected value"
    func = "func1"
    actual = func1(1)
    if expected == actual:
        print _fmtPassed.format("func1(params)")
    else:
        print _fmtFailed.format(func, expected, actual)

    # Test case 2 ...


if __name__ == '__main__':
    main()
