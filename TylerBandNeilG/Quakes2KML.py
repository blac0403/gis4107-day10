#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Neil
#
# Created:     10-11-2016
# Copyright:   (c) Neil 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import sys

_fmtPassed = "Passed: {}"
_fmtFailed = "Failed: {}\n  Expect: {}\n  Actual: {}"
_scriptFolder = os.path.dirname(os.path.abspath(__file__))

def main():
    #test_getKmlPlacemark()
    test_exportToKml()

def exportToKml(inFile, outKml):
    kmlList = []
    outFile = open(outKml, 'w')
    for inText in open(inFile):
        #inFile.readlines()[1:]
        list(inText)
        kmlList.append(inText)
        [x.strip() for x in kmlList.split(',')]

        lat = kmlList[0]
        lon = kmlList[0]
        depth = kmlList[0]
        mag = kmlList[0]

        header = getKmlHeader()
        body = getKmlPlacemark(lon,lat,depth,mag)
        footer = getKmlFooter()

        outFile.write(header +body +footer)

    print kmlList

    outFile.close()


def getKmlHeader():
    return " <?xml version=1.0 encoding=UTF-8?> \n <kml xmlns=http://www.opengis.net/kml/2.2>"


def getKmlPlacemark(longitude, latitude, depth, magnitude):
    return " <Placemark> \n  <name> %s </name> \n  <description> Mag=%s, Depth =%s km  </description> \n  <Point> \n   <coordinates>%s,%s</coordinates> \n  </Point>\n  </Placement>" % (magnitude,magnitude,depth,longitude,latitude)

def getKmlFooter():
    return "</Document> \n </kml>"

def test_getKmlPlacemark():
    print getKmlPlacemark(-116.355, 34.692, 12.3, 1.21)

def test_exportToKml():
    exportToKml(r"C:\acgis\gis4107\day10\lab\TylerBandNeilG\TylerBandNeilG\quakes2000\quakes2000.txt", "Kml_quakes2000.txt")

if __name__ == '__main__':
    main()


##
### Test case 1
##    expected = "expected value"
##    func = "func1"
##    actual = func1(1)
##    if expected == actual:
##        print _fmtPassed.format("func1(params)")
##    else:
##        print _fmtFailed.format(func, expected, actual)
##
##    # Test case 2 ...
