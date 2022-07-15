from render import *

r = None

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

def glFinish():
    global r 
    r.write('a.bmp')



