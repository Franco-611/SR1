import struct
from color import *
from vector import *

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

        b = round(self.pixels[y][x][0] * intensity)
        g = round(self.pixels[y][x][1] * intensity)
        r = round(self.pixels[y][x][2] * intensity)

        return color(
            max(min(r, 255), 0),
            max(min(g, 255), 0),
            max(min(b, 255), 0)
        )

def sobre_textura(figura, r, t):

    for face in figura.caras:

        if len(face) == 4:
            f1 = face[0][1] - 1
            f2 = face[1][1] - 1
            f3 = face[2][1] - 1
            f4 = face[3][1] - 1

            v1 = V3(
                figura.tvertices[f1][0] * t.width,
                figura.tvertices[f1][1] * t.height
            )

            v2 = V3(
                figura.tvertices[f2][0] * t.width,
                figura.tvertices[f2][1] * t.height
            )

            v3 = V3(
                figura.tvertices[f3][0] * t.width,
                figura.tvertices[f3][1] * t.height
            )
            v4 = V3(
                figura.tvertices[f4][0] * t.width,
                figura.tvertices[f4][1] * t.height
            )
            r.line(v1,v2)
            r.line(v2,v3)
            r.line(v3,v4)
            r.line(v4,v1)



        elif len(face) == 3:
            f1 = face[0][1] - 1
            f2 = face[1][1] - 1
            f3 = face[2][1] - 1

            v1 = V3(
                figura.tvertices[f1][0] * t.width,
                figura.tvertices[f1][1] * t.height
            )

            v2 = V3(
                figura.tvertices[f2][0] * t.width,
                figura.tvertices[f2][1] * t.height
            )

            v3 = V3(
                figura.tvertices[f3][0] * t.width,
                figura.tvertices[f3][1] * t.height
            )
            r.line(v1,v2)
            r.line(v2,v3)
            r.line(v3,v1)
            
    r.write()





