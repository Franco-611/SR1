import random
from tkinter import Y
from WriteUtilities import *
from color import *
from Obj import *
from vector import *
from textures import *
from matriz import *
from math import *

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
        self.texture = None
        self.A_shader = None
        self.arregloTringulo=[]
        self.luz=V3(1,0.5,-1)
        self.Model = None
        self.View = None
        self.Proy = None
        self.ViewPort = None
        self.A_shader = None
        self.clear()
        self.colortemporal =[0,0,0]

    def loadModelMatrix(self, translate=(0,0,0), scale=(1,1,1), rotate=(0,0,0)):
        translate = V3(*translate)
        rotate = V3(*rotate)
        scale = V3(*scale)

        translate_matrix = MAT([
            [1,0,0,translate.x],
            [0,1,0,translate.y],
            [0,0,1,translate.z],
            [0,0,0,1]
        ]
        )

        scale_matrix = MAT([
            [scale.x,0,0,0],
            [0,scale.y,0,0],
            [0,0,scale.z,0],
            [0,0,0,1]
        ]
        )

        a = rotate.x
        # cambie
        rotacionX = MAT([
            [1,0,0,0],
            [0,cos(a),-sin(a),0],
            [0,sin(a),cos(a),0],
            [0,0,0,1]
        ]
        )

        b = rotate.y
        rotacionY = MAT([
            [cos(b),0,sin(b),0],
            [0,1,0,0],
            [-sin(b),0,cos(b),0],
            [0,0,0,1]
        ]
        )

        c = rotate.z
        rotacionZ = MAT([
            [cos(c),-sin(c),0,0],
            [sin(c),cos(c),0,0],
            [0,0,1,0],
            [0,0,0,1]
        ]
        )

        rot = rotacionX *  rotacionY * rotacionZ

        self.Model = translate_matrix * rot * scale_matrix 

    def loadViewMatrix(self, x, y, z, center):
        Mi = MAT([
            [x.x, x.y, x.z, 0],
            [y.x, y.y, y.z, 0],
            [z.x, z.y, z.z, 0], 
            [0,0,0,1]

        ])

        O = MAT([
            [1, 0, 0, -center.x],
            [0, 1, 0, -center.y],
            [0, 0, 1, -center.z],
            [0, 0, 0,         1]
        ])

        self.View = Mi * O

    def loadProjection(self):

        self.Proy = MAT([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, -0.001, 1]
        ])

    def loadViewport(self):
        x=self.x0
        y=self.y0
        w= self.widthV
        h= self.heightV


        self.ViewPort = MAT([
            [w, 0, 0, x+w],
            [0, h, 0, y+h],
            [0, 0, 128, 128],
            [0, 0, 0, 1]
        ])

    def lookAt(self, eye, center, up):
        eye = V3(*eye)
        center = V3(*center)
        up = V3(*up)

        z = (eye-center).norm()
        x = (up * z).norm()
        y = (z * x).norm()

        self.loadViewMatrix(x,y,z, center)
        self.loadProjection()
        self.loadViewport()

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
        self.colortemporal = [r,g,b]
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
                if y < self.height and x < self.width:
                    f.write(self.framebuffer[y][x])
            f.write(bytes(extra_bytes[0:offset]))

        f.close()

    def point(self, x, y):
        if x < self.width and x >= 0 and y >= 0 and y < self.height:
            #print(self.colorD)
            self.framebuffer[x-1][y-1]= self.colorD

    def line(self, v1,v2):
        x0= round(v1.x) 
        y0= round(v1.y)
        x1= round(v2.x)
        y1= round(v2.y)

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

    def transformar(self, vertex):
        augmented_vertex = MAT([
            [vertex[0]],
            [vertex[1]],
            [vertex[2]],
            [1]
        ]
        )
        transforVertex = self.ViewPort * self.Proy * self.View * self.Model  * augmented_vertex  
        transforVertex = transforVertex.mat

        result = V3(
            transforVertex[0][0] / transforVertex[3][0],
            transforVertex[1][0] / transforVertex[3][0],
            transforVertex[2][0] / transforVertex[3][0],
        )
        # print(result)
        return result

    def diseno3D(self, objeto, escala, traslacion, rotacion = (0, 0, 0)):
        self.loadModelMatrix(traslacion, escala, rotacion)
        obje = Obj(objeto)
        for i in obje.caras:
            if len(i) == 4:
                f1 = i[0][0] - 1
                f2 = i[1][0] - 1
                f3 = i[2][0] - 1
                f4 = i[3][0] - 1

                v1 = self.transformar(obje.vertices[f1])
                v2 = self.transformar(obje.vertices[f2])
                v3 = self.transformar(obje.vertices[f3])
                v4 = self.transformar(obje.vertices[f4])


                if self.texture:
                    ft1 = i[0][1] - 1
                    ft2 = i[1][1] - 1
                    ft3 = i[2][1] - 1
                    ft4 = i[3][1] - 1

                    vt1 = V3(*obje.tvertices[ft1])
                    vt2 = V3(*obje.tvertices[ft2])
                    vt3 = V3(*obje.tvertices[ft3])
                    vt4 = V3(*obje.tvertices[ft4])

                    # Cambio de self.shader a self.A_shader
                    if (self.A_shader != None):
                        fn1 = i[0][2] - 1
                        fn2 = i[1][2] - 1
                        fn3 = i[2][2] - 1
                        fn4 = i[3][2] - 1

                        vn1 = self.transformar(obje.nvertices[fn1])
                        vn2 = self.transformar(obje.nvertices[fn2])
                        vn3 = self.transformar(obje.nvertices[fn3])
                        vn4 = self.transformar(obje.nvertices[fn4])

                        self.arregloTringulo.append(v1)
                        self.arregloTringulo.append(v2)
                        self.arregloTringulo.append(v3)
                        self.arregloTringulo.append(vt1)
                        self.arregloTringulo.append(vt2)
                        self.arregloTringulo.append(vt3)
                        self.arregloTringulo.append(vn1)
                        self.arregloTringulo.append(vn2)
                        self.arregloTringulo.append(vn3)

                        self.arregloTringulo.append(v1)
                        self.arregloTringulo.append(v3)
                        self.arregloTringulo.append(v4)
                        self.arregloTringulo.append(vt1)
                        self.arregloTringulo.append(vt3)
                        self.arregloTringulo.append(vt4)
                        self.arregloTringulo.append(vn1)
                        self.arregloTringulo.append(vn3)
                        self.arregloTringulo.append(vn4)

                    else:
                        self.arregloTringulo.append(v1)
                        self.arregloTringulo.append(v2)
                        self.arregloTringulo.append(v3)
                        self.arregloTringulo.append(vt1)
                        self.arregloTringulo.append(vt2)
                        self.arregloTringulo.append(vt3)

                        self.arregloTringulo.append(v1)
                        self.arregloTringulo.append(v3)
                        self.arregloTringulo.append(v4)
                        self.arregloTringulo.append(vt1)
                        self.arregloTringulo.append(vt3)
                        self.arregloTringulo.append(vt4)

                else:
                    # Cambio de self.shader a self.A_shader
                    if (self.A_shader != None):
                        fn1 = i[0][2] - 1
                        fn2 = i[1][2] - 1
                        fn3 = i[2][2] - 1
                        fn4 = i[3][2] - 1

                        vn1 = self.transformar(obje.nvertices[fn1])
                        vn2 = self.transformar(obje.nvertices[fn2])
                        vn3 = self.transformar(obje.nvertices[fn3])
                        vn4 = self.transformar(obje.nvertices[fn4])

                        self.arregloTringulo.append(v1)
                        self.arregloTringulo.append(v2)
                        self.arregloTringulo.append(v3)
                        self.arregloTringulo.append(vn1)
                        self.arregloTringulo.append(vn2)
                        self.arregloTringulo.append(vn3)

                        self.arregloTringulo.append(v1)
                        self.arregloTringulo.append(v3)
                        self.arregloTringulo.append(v4)
                        self.arregloTringulo.append(vn1)
                        self.arregloTringulo.append(vn3)
                        self.arregloTringulo.append(vn4)

                    else:
                        self.arregloTringulo.append(v1)
                        self.arregloTringulo.append(v2)
                        self.arregloTringulo.append(v3)

                        self.arregloTringulo.append(v1)
                        self.arregloTringulo.append(v3)
                        self.arregloTringulo.append(v4)


            elif len(i) == 3:
                f1 = i[0][0] - 1
                f2 = i[1][0] - 1
                f3 = i[2][0] - 1

                v1 = self.transformar(obje.vertices[f1])
                v2 = self.transformar(obje.vertices[f2])
                v3 = self.transformar(obje.vertices[f3])
                
                if self.texture:

                    ft1 = i[0][1] - 1
                    ft2 = i[1][1] - 1
                    ft3 = i[2][1] - 1


                    vt1 =  V3(*obje.tvertices[ft1])
                    vt2 =  V3(*obje.tvertices[ft2])
                    vt3 =  V3(*obje.tvertices[ft3])
                    
                    
                    self.arregloTringulo.append(v1)
                    self.arregloTringulo.append(v2)
                    self.arregloTringulo.append(v3)
                    self.arregloTringulo.append(vt1)
                    self.arregloTringulo.append(vt2)
                    self.arregloTringulo.append(vt3)

                else:
                    self.arregloTringulo.append(v1)
                    self.arregloTringulo.append(v2)
                    self.arregloTringulo.append(v3)

                # Cambio de self.shader a self.A_shader
                if (self.A_shader != None):
                        fn1 = i[0][2] - 1
                        fn2 = i[1][2] - 1
                        fn3 = i[2][2] - 1


                        vn1 = self.transformar(obje.nvertices[fn1])
                        vn2 = self.transformar(obje.nvertices[fn2])
                        vn3 = self.transformar(obje.nvertices[fn3])

                        self.arregloTringulo.append(vn1)
                        self.arregloTringulo.append(vn2)
                        self.arregloTringulo.append(vn3)
        self.dibujar()
                    
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
        w = 1 - (cx + cy) / cz
        return (w, u, v)

    def dibujar(self):
        self.arregloTringulo = iter(self.arregloTringulo)

        try:
            while(True):
                self.tringulo()

        except:
          StopIteration

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

    def tringulo(self):
        A = next(self.arregloTringulo)
        B = next(self.arregloTringulo)
        C = next(self.arregloTringulo)
        tA = V3(0, 0, 0)
        tB = V3(0, 0, 0)
        tC = V3(0, 0, 0)
        nA = V3(0, 0, 0)
        nB = V3(0, 0, 0)
        nC = V3(0, 0, 0)
        if self.texture:
            tA = next(self.arregloTringulo)
            tB = next(self.arregloTringulo)
            tC = next(self.arregloTringulo)
        
        if (self.A_shader != None):
            nA = next(self.arregloTringulo)
            nB = next(self.arregloTringulo)
            nC = next(self.arregloTringulo)

        l = self.luz
        n = (C-A) * (B-A)
        i = n.norm() @ l.norm()
        
        Bmin , Bmax = self.bounding_box(A,B,C)
        for x in range(round(Bmin.x), round(Bmax.x+1)):
            for y in range(round(Bmin.y), round(Bmax.y+1)):
                w,u,v = self.barycentric(A,B,C,V3(x,y))
                
                # print(x, y)
                
                if (w < 0 or v < 0 or u < 0):
                    #print('pase')
                    continue
                # print(w, u , v)
                z = A.z * w + B.z * v + C.z * u

                if y >= 0 and x >= 0 and y < self.height and x < self.width and self.zbuffer[x][y] < z:
                    self.zbuffer[x][y] = z
                    # Cambio de self.shader a self.A_shader
                    if (self.A_shader):
                        self.colorD = self.A_shader(
                            vertices = (A,B,C),
                            texturas = (tA, tB, tC),
                            normales = (nA, nB, nC), 
                            bar = (w, v, u), 
                            luz = self.luz,
                            height = y,
                            width = x,
                            iii = i
                        )

                    else:
                        if self.texture:
                            tx = tA.x * w + tB.x * u + tC.x * v
                            ty = tA.y * w + tB.y * u + tC.y * v

                            self.colorD = self.texture.get_color_with_intensity(tx, ty, i)

                    self.point(y,x)  
    
    def asignar(self):
        self.A_shader = self.shader

    def shader(self, **kwargs):
        A, B, C = kwargs['vertices']
        w, v, u = kwargs['bar']
        tA, tB, tC = kwargs['texturas']
        nA, nB, nC = kwargs['normales']

        y = kwargs['height']
        x = kwargs['width']

        ni = kwargs['iii']


        l = V3(0,0,-1)
        iA = nA.norm() @ l.norm()
        iB = nB.norm() @ l.norm()
        iC = nC.norm() @ l.norm()

        i = iA * w + iB * u + iC * v

        i = -i * 6
        
        if self.texture:
            
            tx = tA.x * w + tB.x * u + tC.x * v
            ty = tA.y * w + tB.y * u + tC.y * v

            return self.texture.get_color_with_intensity(tx, ty, -i)

        else:

            if y >= 1525 or y <= 575:
                primer = random.randint(1, 3)

                if primer == 1:
                    return color(round(226*i), round(221*i), round(144*i))
                elif primer == 2:
                    return color(round(250*i), round(239*i), round(221*i))
                elif primer == 3:
                    return color(round(191*i), round(186*i), round(129*i))

            else:
                if y <= 1100 and y >= 805  and x <= 1300 and x >= 900:
                    
                    segundo = random.randint(1, 10)

                    if segundo == 1:
                        return color(round(228*ni), round(102*ni), round(57*ni))
                    elif segundo == 2:
                        return color(round(192*ni), round(88*ni), round(57*ni))
                    elif segundo == 3:
                        return color(round(174*ni), round(113*ni), round(94*ni))
                    elif segundo == 4:
                        return color(round(228*ni), round(102*ni), round(57*ni))
                    elif segundo == 5:
                        return color(round(228*ni), round(102*ni), round(57*ni))
                    elif segundo == 6:
                        return color(round(228*ni), round(102*ni), round(57*ni))
                    if segundo == 7:
                        return color(round(228*ni), round(102*ni), round(57*ni))
                    elif segundo == 8:
                        return color(round(92*ni), round(54*ni), round(43*ni))
                    elif segundo == 9:
                        return color(round(174*ni), round(113*ni), round(94*ni))
                    elif segundo == 10:
                        return color(round(92*ni), round(54*ni), round(43*ni))
                        

                else:

                    segundo = random.randint(1, 10)


                    if segundo == 1:
                        return color(round(228*ni), round(102*ni), round(57*ni))
                    elif segundo == 2:
                        return color(round(192*ni), round(88*ni), round(57*ni))
                    elif segundo == 3:
                        return color(round(174*ni), round(113*ni), round(94*ni))
                    elif segundo == 4:
                        return color(round(228*ni), round(102*ni), round(57*ni))
                    elif segundo == 5:
                        return color(round(228*ni), round(102*ni), round(57*ni))
                    elif segundo == 6:
                        return color(round(228*ni), round(102*ni), round(57*ni))
                    if segundo == 7:
                        return color(round(228*ni), round(102*ni), round(57*ni))
                    elif segundo == 8:
                        return color(round(92*ni), round(54*ni), round(43*ni))
                    elif segundo == 9:
                        return color(round(174*ni), round(113*ni), round(94*ni))
                    elif segundo == 10:
                        return color(round(92*ni), round(54*ni), round(43*ni))
    
    def background(self, archivo):
        imagen = Textures(archivo)
        self.framebuffer=imagen.pixels

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
