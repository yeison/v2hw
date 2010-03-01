#Yeison Rodriguez
#!/usr/bin/env python
from opencv import highgui, cv
from types import NoneType


class Graph:
    def __init__(self, image):
        try:
            self.image = highgui.cvLoadImage(image, highgui.CV_LOAD_IMAGE_GRAYSCALE)
            if(type(self.image) == NoneType):
                print >> sys.stderr, "  The filename provided does not exist."
                sys.exit(1)
        except IndexError as e:
            print >> sys.stderr, "  Please provide the name of a local image."
            sys.exit(1)


class PixelArray:
    pxArray = {}
    def getPixel(theta, coords):
        return pxArray[coords[0], coords[1], theta]
    def addPixel(pixelNode):
        pxArray.append(pixelNode)
    def __init__(self, imageGraph):
        
        print "Made pxNodeArray" 

#A node is defined by the pixel's location and theta.
class PixelNode:
    #Fill with u's and v's
    grayValue = None
    x = None
    y = None
    angle = None
    costFromA = None #maybe?
    
    def __init__(theta, coords):
        angle = theta
        x = coords[0]
        y = coords[1]

class Coordinates(list):
    
    def __init__(self, x, y):
        self.append(x)
        self.append(y)
        self.x = x
        self.y = y
