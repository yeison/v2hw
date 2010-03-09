from PixelNode import PixelArray
from math import pi
import sys

thetas = [-pi/2, -pi/4, 0, pi/4, pi/2, (3*pi)/4, pi, (5*pi)/4]

class ContourDetector:
    def __init__(self, pxArray, C, startPx):
        #pxArray.n is the number of pixels for a black and white image.
        for p in range(pxArray.n):
            for theta in thetas:
                try:
                    if(pxArray.list[p] == startPx):
                        print "I am startPx"
                except IndexError as e:
                    print >> sys.stderr, "IndexError: pixel %s does not exist" % p
                    raise

scale = 3

pxArray = PixelArray("circle.jpg", scale)

print "There are %s pixels" % pxArray.n                                                   

cd = ContourDetector(pxArray, 3, pxArray[5, 10, 0])
