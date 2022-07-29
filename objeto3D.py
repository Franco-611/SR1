from gl import *
from render import *

glInit()
glCreateWindow(800,800)
glClearColor(0,0,0)
glClear()
glObjeto3D('face.obj', (20,20),(400,150))
glFinish('cara.bmp')
