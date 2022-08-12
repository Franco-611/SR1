from gl import *
from render import *

glInit()
glCreateWindow(2000,2000)
glClearColor(0,0,0)
glClear()
glColor(1,0.5,0)
#glObjeto3D('cara.obj', (700,700,700),(1000,1000,600))
glObjeto3D('Among.obj', (1.5,1.5,1.5),(1000,400,600))
#glZbuffer('Zbuffer.bmp')
glFinish('sr4.bmp')