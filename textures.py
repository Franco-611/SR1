import struct
from color import *
from render import *

class Textures:
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        with open(self.path, "rb") as image:
            image.seek(2 + 4 + 2 + 2)
            header_size = struct.unpack("=l", image.read(4))[0]
            image.seek(2 + 4 + 2 + 2 + 4 + 4)
            self.width = struct.unpack("=l", image.read(4))[0]
            self.height = struct.unpack("=l", image.read(4))[0]

            image.seek(header_size)

            self.pixels = []
            for y in range(self.height):
                self.pixels.append([])
                for x in range(self.width):
                    b = ord(image.read(1))

                    g = ord(image.read(1))
                    r = ord(image.read(1))
                    self.pixels[y].append(
                        color(r, g, b)
                    )

    def get_color(self, tx, ty):
        x = round(tx * self.width)
        y = round(ty * self.height)

        return self.pixels[y][x]

    def get_color_with_intensity(self, tx, ty, intensity):
        x = round(tx * self.width)
        y = round(ty * self.height)

        b = self.pixels[y][x][0] * intensity
        g = self.pixels[y][x][1] * intensity
        r = self.pixels[y][x][2] * intensity

        return color(r, g, b)

r = Render(250,250)
t = Textures("model.bmp")
r.width=t.width
r.height= t.height
r.framebuffer=t.pixels
r.write()

figura = Obj("cara.obj")
w=[t.width,t.height,0]
e=[0,0,0]
r.Color(1,0,0)


for face in figura.caras:
    
    f1 = face[0][1] - 1
    f2 = face[1][1] - 1
    f3 = face[2][1] - 1

    v1 = r.transformar(figura.tvertices[f1],w,e)
    v2 = r.transformar(figura.tvertices[f2],w,e)
    v3 = r.transformar(figura.tvertices[f3],w,e)

    r.triangulo(v1,v2,v3)
        
r.write()

