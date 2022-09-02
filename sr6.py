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

'''
#Medium Shot
glLook((1.2,1.7,1),(0,1.5,0),(0,1,0))
glObjeto3D('cofre.obj', (1.5, 1.5, 1.5),(-0.3,0,0), (-0.02,-0.4,0))
glFinish('sr6MediumShot.bmp')
'''

'''
#Low angle Shot
glLook((1.2,1,1),(0,1.5,0),(0,1,0))
glObjeto3D('cofre.obj', (1.5, 1.5, 1.5),(-0.3,0,0), (-0.02,-0.4,0))
glFinish('sr6LowShot.bmp')
'''

'''
#High Shot
glLook((1.2,3,1),(0,1.5,0),(0,1,0))
glObjeto3D('cofre.obj', (1.5, 1.5, 1.5),(-0.3,0,0), (-0.02,-0.4,0))
glFinish('sr6HighShot.bmp')
'''

'''
#Dutch Shot
glLook((1.2,1.7,1),(0,1.7,0.55),(-0.8,1,0))
glObjeto3D('cofre.obj', (1.5, 1.5, 1.5),(-0.3,0,0), (-0.02,-0.4,0))
glFinish('sr6DutchShot.bmp')
'''
