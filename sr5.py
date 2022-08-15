from gl import *
from render import *
from textures import *


glInit()
glCreateWindow(2000,2000)
glClearColor(0,0,0)
glClear()
glColor(1,1,0)
t = Textures("model.bmp")
glTexture(t)
glObjeto3D('cara.obj', (800,800,800),(1000,1000,600))
#glObjeto3D('tierra.obj', (1.5,1.5,1),(1000,1000,1000))
glFinish('pruebas.bmp')

'''
r = Render(250,250)
t = Textures("model.bmp")
r.width=t.width
r.height= t.height
r.framebuffer=t.pixels
r.write()

figura = Obj("cara.obj")
sobre_textura(figura, r, t)
'''


