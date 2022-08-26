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
#glObjeto3D('cara.obj', (800,800,800),(1000,1000,600))
glLook((100,30,10),(0,1,0), (0,1,0))
glObjeto3D('cofre.obj', (850,850,800),(1000,900,600), (0.4,0.4,0))
#glObjeto3D('tierra.obj', (1.5,1.5,1),(1000,1000,1000))
glFinish('sr5.bmp')

'''
r = Render(4096,4096)
t = Textures("cofre.bmp")
r.Color(int(1*255), int(0*255), int(0*255))
r.width=t.width
r.height= t.height
r.framebuffer=t.pixels
r.write()

figura = Obj("cofre.obj")
sobre_textura(figura, r, t)
'''

