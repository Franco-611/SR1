from gl import *
from render import *

glInit()
glCreateWindow(2000,2000)
glClearColor(0,0,0)
glClear()
glColor(1,1,0)
glObjeto3D('cara.obj', (500,500,500),(1000,600,600))
glFinish('pruebas.bmp')