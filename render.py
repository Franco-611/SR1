from WriteUtilities import *
from color import *

class Render(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.colorN = color(0 , 0, 0) 
        self.clear()

    def clear(self):
        self.framebuffer= [
            [self.colorN for x in range(self.width)]
            for y in range(self.height)
        ]

    def write(self, filename):
        f= open(filename, 'bw')

        # pixel header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(word(0))
        f.write(word(0))
        f.write(dword(14 + 40))

        # info header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(word(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        # pixel data
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])

        f.close()

    def point(self, x, y, c):
        self.framebuffer[x][y]=self.colorN


