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
r.line(80,80,20,10)
r.write('a.bmp')