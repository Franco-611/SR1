from gl import *
from render import *
from textures import *


glInit()
glCreateWindow(2000,2000)
glClearColor(0,0,0)
glClear()
glColor(1,1,0)
t = Textures("cofre.bmp")
glTexture(t)
glViewPort(0,0,1500,1500)
glLook((1,1,1),(0,1,0),(0,1,0))
#glObjeto3D('cofre.obj', (850,850,800),(1000,900,600), (0.4,0.4,0))
glObjeto3D('cofre.obj', (0.7, 0.7, 0.7),(0,0,0), (0.1,0.9,0))
glFinish('sr6.bmp')