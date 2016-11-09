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
    if len(sys.argv) == 3:
        dumpFileList(sys.argv[1], sys.argv[2])
    test_dumpFileList()

def dumpFileList(folder, dumpFile):
    dumpList =[]
    if os.path.exists(folder):
        for fileDir in os.listdir(folder):
            dumpList.append(os.path.abspath(fileDir))

        outFile = open(dumpFile, 'w')
        for fileName in dumpList:
            outFile.write("%s\n"% fileName)
        outFile.close()
        inFile = open(dumpFile, 'r')
        inText= inFile.read()
        inFile.close()
        return inText
    else:
        return folder + " was not found"



def test_dumpFileList():
    expected = r"""C:\acgis\gis4107\day10\lab\TylerBandNeilG\TylerBandNeilG\dumpydump.txt
C:\acgis\gis4107\day10\lab\TylerBandNeilG\TylerBandNeilG\ExerciseTemplate.py
C:\acgis\gis4107\day10\lab\TylerBandNeilG\TylerBandNeilG\fileDemo.txt
C:\acgis\gis4107\day10\lab\TylerBandNeilG\TylerBandNeilG\FileUtils.py
C:\acgis\gis4107\day10\lab\TylerBandNeilG\TylerBandNeilG\NameDumper.py"""
    func = "dumpFileList"
    actual = dumpFileList(r"C:\acgis\gis4107\day10\lab\\TylerBandNeilG", "dumpydump.txt")

    if expected == actual:
        print _fmtPassed.format("func1(params)")
    else:
        print _fmtFailed.format(func, expected, actual)

    # Test case 2 ...


if __name__ == '__main__':
    main()
