from WriteUtilities import *
from color import *
from Obj import *
from vector import *

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
        self.zbuffer= [
            [-9999999999 for x in range(self.width)]
            for y in range(self.height)
        ]
        self. sobrabuffer= [
            [self.colorN for x in range(self.width)]
            for y in range(self.height)
        ]

    def write(self, filename="pruebass.bmp"):
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
        for y in range(self.height):
            for x in range(self.width):
                f.write(self.framebuffer[y][x])
            f.write(bytes(extra_bytes[0:offset]))

        f.close()

    def point(self, x, y):
        if not (x > self.width and x < 0 and y < 0 and y > self.height):
            self.framebuffer[x][y]=self.colorD

    def line(self, v1,v2):
        x0= v1.x 
        y0= v1.y
        x1= v2.x
        y1= v2.y

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

        for x in range (x0,x1+1):
            if Empinado:
                self.point(x, y)
            else:
                self.point(y, x)

            offset += dy * 2

            if offset >= threshold:
                y += 1 if y0 < y1 else -1
                threshold += dx * 2

    def transformar(self, punto, escala, tras):
        result = V3(
            (punto[0] * escala[0] + tras[0]),
            (punto[1] * escala[1] + tras[1]),
            (punto[2] * escala[2] + tras[2])
        )
        return result

    def diseno3D(self, objeto, escala, traslacion):
        obje = Obj(objeto)
        for i in obje.caras:
            if len(i) == 4:
                f1 = i[0][0] - 1
                f2 = i[1][0] - 1
                f3 = i[2][0] - 1
                f4 = i[3][0] - 1

                v1 = self.transformar(obje.vertices[f1], escala, traslacion)
                v2 = self.transformar(obje.vertices[f2], escala, traslacion)
                v3 = self.transformar(obje.vertices[f3], escala, traslacion)
                v4 = self.transformar(obje.vertices[f4], escala, traslacion)

                self.tringulo(v1, v2, v3)
                self.tringulo(v1, v3, v4)

            elif len(i) == 3:
                f1 = i[0][0] - 1
                f2 = i[1][0] - 1
                f3 = i[2][0] - 1

                v1 = self.transformar(obje.vertices[f1], escala, traslacion)
                v2 = self.transformar(obje.vertices[f2], escala, traslacion)
                v3 = self.transformar(obje.vertices[f3], escala, traslacion)

                self.tringulo(v1, v2, v3)

            '''
            for x in range(len(i)):


                vert1 = i[x][0] - 1
                vert2 = i[(x+1)%len(i)][0] - 1

                punt1= self.transformar(obje.vertices[vert1], escala, traslacion)

                punt2= self.transformar(obje.vertices[vert2], escala, traslacion)

                self.line(punt1[0],punt1[1],punt2[0],punt2[1])

            '''

    def barycentric(self,A, B, C, P):
        cx, cy, cz = self.cross(
            V3(B.x - A.x, C.x - A.x, A.x - P.x),
            V3(B.y - A.y, C.y - A.y, A.y - P.y)
        )

        if cz==0:
            cz=1
        try:
            u = cx / cz
        except:
            print('1',cx,'2',cy,'3',cz)
        v = cy / cz
        w = 1 - (cx + cy)/cz
        return (w, v, u)

    def cross(self,v1,v2):
        return(
            v1.y * v2.z - v1.z * v2.y,
            v1.z * v2.x - v1.x * v2.z,
            v1.x * v2.y - v1.y * v2.x
        )

    def bounding_box(self,A,B,C):
            xs=[A.x,B.x,C.x]
            ys=[A.y,B.y,C.y]
            
            xs.sort()
            ys.sort()
            return V3(xs[0],ys[0]),V3(xs[-1],ys[-1])

    def tringulo(self,A,B,C):
        l = V3(0,0,-1)
        n = (C-A) * (B-A)
        i = n.norm() @ l.norm()

        if i<= 0 or i>1:
            return

        self.colorD = color(round(25*i*10), round(25*i*10), round(25*i*10))

        Bmin , Bmax = self.bounding_box(A,B,C)
        for x in range(round(Bmin.x), round(Bmax.x+1)):
            for y in range(round(Bmin.y), round(Bmax.y+1)):
                w,v,u = self.barycentric(A,B,C,V3(x,y))

                if (w < 0 or v < 0 or u < 0):
                    continue
                
                z = A.z * w + B.z * v + C.z * u

                f = z/self.width
                
                if self.zbuffer[x][y] < z:
                    self.zbuffer[x][y] = z
                    self. sobrabuffer[x][y] = color(round(255*f), round(255*f), round(255*f))
                    self.point(x,y)

    def triangulo(self, v1, v2, v3):
        self.line(v1,v2)
        self.line(v2,v3)
        self.line(v3,v1)

    def writeZ(self, filename):
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
                f.write(self. sobrabuffer[y][x])
            f.write(bytes(extra_bytes[0:offset]))

        f.close()

                




