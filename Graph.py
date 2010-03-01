#Yeison Rodriguez
#!/usr/bin/env python
from opencv import highgui, cv
from types import NoneType


class Image(cv.CvMat):
    def __init__(self, filename):
        try:
            self = highgui.cvLoadImage(image, highgui.CV_LOAD_IMAGE_GRAYSCALE)
            if(type(self) == NoneType):
                print >> sys.stderr, "  The filename provided does not exist."
                sys.exit(1)
        except IndexError as e:
            print >> sys.stderr, "  Please provide the name of a local image."
            sys.exit(1)


class PixelArray(dict):
    def copyImage(self, image):
        width = image.width
        height = image height
        for i in width:
            for j in height:
                p = PixelNode(i, j, theta, image[i, j])
                self.addPixel(p)
    def getPixel(self, x, y, theta):
        return self[x, y, theta]
    def addPixel(self, pixel):
        self[pixel.x, pixel.y, pixel.angle] = pixel
    def __init__(self, imageGraph):
        dict.__init__(self)
        
        print "Made pxNodeArray" 
    def __getitem__(self, key):
        return dict.__getitem__(self, key)


#A node is defined by the pixel's location and theta.
class PixelNode:
    #Fill with u's and v's
    costFromA = None #maybe?
    
    def __init__(x, y, theta, grayValue):
        self.angle = theta
        self.x = x
        self.y = y
        self.grayValue = grayValue
