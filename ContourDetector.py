from PixelNode import PixelArray
from math import pi
import sys, copy

thetas = [-pi/2, -pi/4, 0, pi/4, pi/2, (3*pi)/4, pi, (5*pi)/4]

class ContourDetector:
    back = {}

    def optimal(self, endPx, gamma):
        newPxArray = copy.copy(self.pxArray)

        for v in range(newPxArray.n):
            if self.pxArray[v].weight < 100000:
                for u in range(len(thetas)):
                    newPxArray.setWeight(newPxArray.list[v + u], self.pxArray.list[v], gamma)
        
        for tau in range(2, C+1):
            for v in range(newPxArray.n):
                pathCost = 100000
                if self.pxArray.list[v].weight < 100000:
                    newCost =  self.pxArray.list[v].weight + newPxArray.list[v].weight)
                    if newCost < pathCost:
                        pathCost = newCost
                        back[v] = self.pxArray.list[v]
            
            
            

    def __init__(self, pxArray, C, startPx):
        self.C = C
        self.pxArray = pxArray
        #pxArray.n is the number of pixels for a black and white image.
        #pxArray is an uninitialized phi at tau = 1
        #p is a pixel and angle
        for p in range(pxArray.n):
            try:
                if(pxArray.list[p] == startPx):
                    pxArray.setContrast(pxArray.list[p])
                    pxArray.list[p].weight = pxArray.list[p].contrast
                else:
                    pxArray.list[p].contrast = 100000
            except IndexError as e:
                print >> sys.stderr, "IndexError: pixel %s does not exist" % p
                raise

scale = 3

pxArray = PixelArray("circle.jpg", scale, thetas)

print "There are %s pixel and angle combinations" % pxArray.n                                                   

cd = ContourDetector(pxArray, 3, pxArray[5, 10, 0])
