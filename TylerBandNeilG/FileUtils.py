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
    test_writeToFile()
    test_getFileContent()

def writeToFile(fileName, content):
    outfile = open(fileName, 'w')
    outfile.write(content)
    outfile.close()

def getFileContent(fileName):
    try:
        inFile = open(fileName)
        inText = inFile.read()
        inFile.close()
        return inText
    except IOError:
        return fileName + " does not exist."


def test_writeToFile():
    expected = "Some junk text."
    func = 'writeToFile'
    fileName = os.path.join(_scriptFolder,"fileDemo.txt")
    inText = open(fileName)
    actual = inText.read()
    inText.close()
    if expected == actual:
        print _fmtPassed.format("writeToFile(fileName, content)")
    else:
        print _fmtFailed.format(func, expected, actual)

def test_getFileContent():
    expected = "Some junk text."
    func = getFileContent
    actual = getFileContent(os.path.join(_scriptFolder,"fileDemo.txt"))
    if expected == actual:
        print _fmtPassed.format("getFileContent(fileName)")
    else:
        print _fmtFailed.format(func, expected, actual)
#When a file doesn't exist we get an IOError.
    expected = os.path.join(_scriptFolder,"fileDem.txt") + " does not exist."
    func = getFileContent
    actual = getFileContent(os.path.join(_scriptFolder,"fileDem.txt"))
    if expected == actual:
        print _fmtPassed.format("getFileContent(fileName)")
    else:
        print _fmtFailed.format(func, expected, actual)


if __name__ == '__main__':
    main()
