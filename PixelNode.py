#Yeison Rodriguez
#!/usr/bin/env python
from opencv import highgui, cv
from types import NoneType
from ImageAnalyzer import dofIA2

class PixelArray(dict):
    def contrast(self, pixel):
        T = 1
        contr = T/(abs(dofIA2(pixel.x, pixel.y, pixel.angle, self.scale, self.image)) + 1)
        return contr

    def copyImage(self, image):
        theta = 0
        width = range(self.scale-1, image.width-self.scale)
        height = range(self.scale-1, image.height-self.scale)
        for i in width:
            for j in height:
                p = PixelNode(i, j, theta, image[i, j])
                self.addPixel(p)
                p.contrast = self.contrast(p)

    def getPixel(self, x, y, theta):
        return self[x, y, theta]


    def addPixel(self, pixel):
        self[pixel.x, pixel.y, pixel.angle] = pixel
        self.list.append(pixel)
        

    def __init__(self, filename, scale):
        self.list = []
        self.scale = scale
        try:
            self.image = highgui.cvLoadImage(filename, highgui.CV_LOAD_IMAGE_GRAYSCALE)
            #Deal with borders and performing analyses.
            self.n = (self.image.width - (scale + 2)) * (self.image.height - (scale + 2))
            if(type(self.image) == NoneType):
                print >> sys.stderr, "  The filename provided does not exist."
                sys.exit(1)
        except IndexError as e:
            print >> sys.stderr, "  Please provide the name of a local image."
            sys.exit(1)        
        dict.__init__(self)
        self.default = None
        self.copyImage(self.image)
        
    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            print >> sys.stderr, "  The specified pixel is not accessible.  It might not exist"
            return self.default

#A node is defined by the pixel's location and theta.
class PixelNode(list):
    #Fill with u's and v's
    #costFromA = None #maybe?
    contrast = None

    def __init__(self, x, y, theta, grayValue):
        self.append(x)
        self.x = self[0]
       
        self.append(y)
        self.y = self[1]

        self.append(theta)
        self.angle = self[2]

        self.append(grayValue)
        self.grayValue = self[3]

    def __print__(self):
        print "x:%s  y:%s  theta:%s  gray:%s" % (self.x, self.y, self.angle, self.grayValue)


#scale = 3

#pxArray = PixelArray("circle.jpg", scale)

#print "There are %s pixels" % pxArray.n

#for i in range(scale, 100-scale):
#    for j in range(scale, 100-scale):
#        print  pxArray.contrast(pxArray[i, j, 0])
