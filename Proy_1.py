from gl import *
from render import *
from textures import *


glInit()
glCreateWindow(800,836)
glClearColor(1,1,1)
glClear()
glFondo("cubierta.bmp")
glColor(1,0,0)
glShader()

glViewPort(-1,-1,800,836)

glLook((0,0,1),(0,0,0),(0,1,0))


t = Textures("cofre.bmp")
glTexture(t)
glObjeto3D('cofre.obj', (0.15, 0.15, 0.15),(-0.7,-0.8,-0.6), (0.35,0.3,0))

glNuevo()
t = Textures("silla.bmp")
glTexture(t)
glObjeto3D('silla.obj', (0.1, 0.1, 0.1),(-0.68,-0.67,-0.6), (0.2,0.3,0))

glNuevo()
t = Textures("ave.bmp")
glTexture(t)
glObjeto3D('ave.obj', (0.07, 0.07, 0.07),(-0.75,-0.15, -0.3), (0.3,0.8,0))

glNuevo()
t = Textures("barril.bmp")
glTexture(t)
'''
m = Textures("barril2.bmp")
glMap(m)
'''
glObjeto3D('barril.obj', (0.14, 0.14, 0.14),(-0.94, -0.75, -0.8), (0.2,0.3,0))
#glMap(None)


glNuevo()
t = Textures("pirata.bmp")
glTexture(t)
glObjeto3D('pirata.obj', (0.09, 0.09, 0.09),(-0.2,-0.7,0), (0,-0.2,0))


glFinish('Proy1.bmp')
