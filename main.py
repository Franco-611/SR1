from gl import *

glInit()
glCreateWindow(100,100)
glClearColor(0,0,0)
glClear()
glColor(1,0,0)
glLine(-0.6,0.3,-0.3,-0.1)
glLine(-0.6,0,-0.3,-0.4)
glLine(-0.6,0.3,-0.6,0)
glLine(-0.3,-0.1,-0.3,-0.4)
glLine(-0.3,-0.4,0,-0.3)
glLine(0,-0.3,0,-0.15)
glLine(0,-0.15,0.2,-0.05 )

glFinish()



