from WriteUtilities import *
from color import *

class Render:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.widthV = width
        self.heightV = height
        self.x0 = 0
        self.y0 = 0
        self.colorN = color(0, 0, 0) 
        self.colorD = color(250 , 250, 0)
        self.clear()

    def viewPort(self, x, y, wid, hei):
        self.widthV = wid
        self.heightV = hei
        self.x0 = x
        self.y0 = y


    def conversion(self, x, y):
        nuevoX = int (self.x0 + (x+1)* 0.5 * (self.widthV-1))
        nuevoY = int (self.y0 + (y+1)* 0.5 * (self.heightV-1))

        return(nuevoX, nuevoY)


    def ClearColor (self, r, g, b):
        self.colorN = color(r, g, b)

    def Color (self, r, g, b):
        self.colorD = color(r, g, b)

    def clear(self):
        self.framebuffer= [
            [self.colorN for x in range(self.width)]
            for y in range(self.height)
        ]

    def write(self, filename):
        f= open(filename, 'bw')

        offset = (4 - (self.width * 3) % 4) % 4
        new_width = offset + self.width

        # pixel header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + new_width * self.height * 3))
        f.write(word(0))
        f.write(word(0))
        f.write(dword(14 + 40))

        # info header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        extra_bytes = [0, 0, 0]
        # pixel data
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[y][x])
            f.write(bytes(extra_bytes[0:offset]))

        f.close()

    def point(self, x, y):
        self.framebuffer[x][y]=self.colorD

    def line(self, x0, y0, x1, y1):
        dy = abs(y1-y0)
        dx = abs(x1-x0)

        Empinado = dy>dx

        if Empinado:
            x0,y0 = y0,x0
            x1, y1 = y1,x1
 
        if x0>x1:
            x0,x1 = x1,x0
            y0,y1 = y1,y0

        dy = abs(y1-y0)
        dx = abs(x1-x0)

        offset = 0 
        threshold = dx * 2
        y = y0

        for x in range (x0,x1):
            if Empinado:
                self.point(y, x)
            else:
                self.point(x, y)

            offset += dy * 2

            if offset >= threshold:
                y += 1 if y0 < y1 else -1
                threshold += dx * 2

        
