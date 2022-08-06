from gl import *
from render import *

glInit()
glCreateWindow(2000,2000)
glClearColor(0,0,0)
glClear()
glColor(1,1,0)
glObjeto3D('Among.obj', (1.5,1.5,1.5),(1000,400,600))
glFinish('sr3.bmp')
