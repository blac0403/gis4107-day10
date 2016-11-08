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
    test_dumpFileList()

def dumpFileList(folder, dumpFile):
    directory = os.listdir(folder)
    print directory



##    os.listdir(path) os.path.isfile(path), os.path.abspath(path)


def test_dumpFileList():
    pass
    # Test case 1
##    expected = "expected value"
##    func = "func1"
##    actual = func1(1)
##    if expected == actual:
##        print _fmtPassed.format("func1(params)")
##    else:
##        print _fmtFailed.format(func, expected, actual)

    # Test case 2 ...


if __name__ == '__main__':
    main()
