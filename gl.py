from render import *

def glInit():
    print('hola')

def glCreateWindow(width,height):
    print('hola')

def glViewPort(x,y,width,height):
    print('hola')

def glClear():
    print('hola')

def glClearColor(r,g,b):
    print('hola')

def glVertex(x,y):
    print('hola')

def glColor(r,g,b):
    print('hola')

def glFinish():
    print('hola')

r = Render(100, 100)
r.point(25,70)
r.point(75,70)
r.line(80,40,20,40)

r.line(79,40,85,50)

r.line(20,40,14,50)

r.write('a.bmp')
