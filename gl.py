from re import U
from sympy import Max
from render import *
from vector import *

r = None

#Funcion obtenida de Wikipedia -- https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule#:~:text=If%20this%20number%20is%20odd,to%20fill%20in%20strange%20ways
def dentroOno(x: int, y: int, poly) -> bool:
        num = len(poly)
        j = num - 1
        c = False
        for i in range(num):
            if (x == poly[i][0]) and (y == poly[i][1]):
                return True
            if ((poly[i][1] > y) != (poly[j][1] > y)):
                slope = (x-poly[i][0])*(poly[j][1]-poly[i][1])-(poly[j][0]-poly[i][0])*(y-poly[i][1])
                if slope == 0:
                    return True
                if (slope < 0) != (poly[j][1] < poly[i][1]):
                    c = not c
            j = i
        return c

def glInit():
    print('')

def glCreateWindow(w,h):
    global r 
    r = Render(w,h)

def glViewPort(x,y,width,height):
    global r 
    r.viewPort(*r.conversion(x,y),width,height)

def glClear():
    global r 
    r.clear()

def glClearColor(rojo,g,b):
    global r 
    r.ClearColor(int(rojo*255), int(g*255), int(b*255))

def glVertex(x,y):
    global r 
    r.point(*r.conversion(x,y))

def glColor(rojo,g,b):
    global r 
    r.Color(int(rojo*255), int(g*255), int(b*255))

def glLine(x0, y0, x1, y1):
    global r 
    r.line(*r.conversion(x0,y0), *r.conversion(x1,y1))

def glPunto(x,y):
    global r
    r.point(x,y)

def glLinea(x0, y0, x1, y1):
    global r 
    r.line(x0,y0,x1,y1)

def glDelineado(arreglo):
    for elements in range(len(arreglo)):
        glPunto(*arreglo[elements%len(arreglo)])
        glLinea(*arreglo[elements%len(arreglo)],*arreglo[(elements+1)%len(arreglo)])

def glColoreado(arr):
    minX = min([x for x, y in arr])
    maxX = max([x for x, y in arr])
    minY = min([y for x, y in arr])
    maxY = max([y for x, y in arr])
    
    # centroX = int((maxX-minX)/2 + minX)
    # centroY = int((maxY-minY)/2 + minY)
    # centro = [centroX,centroY]

    for i in range(minX , maxX):
        for j in range(minY , maxY):
            if dentroOno(i,j,arr):
                glPunto(i,j)

def glObjeto3D(objeto,escala, traslacion, rotacion=(0,0,0)):
    #print('objeto en gl')
    global r 
    r.diseno3D(objeto,escala,traslacion, rotacion)
    
def glTringulo(A,B,C):
    global r
    r.tringulo(A,B,C)

def glTexture(texture):
    global r
    r.texture = texture

def glZbuffer(nombre):
    global r 
    r.writeZ(nombre)

def glLook(eye, center, up):
    global r 
    r.lookAt(eye, center, up)

def glFondo(textura):
    global r 
    r.background(textura)

def glShader():
    global r
    r.asignar()

def glNuevo():
    global r
    r.nuevo()

def glFinish(nombre):
    global r 
    r.write(nombre)




