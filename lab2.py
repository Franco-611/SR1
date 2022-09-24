from gl import *
from render import *
from textures import *


glInit()
#glCreateWindow(728,475)
glCreateWindow(2000,2000)
glClearColor(1,1,1)
glClear()
glColor(1,1,0)
#glFondo("estrellas.bmp")

glShader()
t = Textures("tierra.bmp")
glTexture(t)

glViewPort(-1,-1,1500,1500)
#glViewPort(0,0,728,475)

glLook((0,0,1),(0,0,0),(0,1,0))
#glLook((0,0,10),(0,0,0),(0,1,0))
glObjeto3D('tierra.obj', (0.001, 0.001, 0.001),(-0.5,-0.5,0), (0,0,0))
# glObjeto3D('cara.obj', (1, 1, 1),(0,0,0), (0,0,0))
#glObjeto3D('cofre.obj', (0.5, 0.5, 0.5),(-0.5,-0.5,0), (0,0,0))
#glObjeto3D('tierra.obj', (0.061,0.061,0.061),(0,0,0),(0,0,0))

glFinish('lab2.bmp')
