from gl import *

glInit()
glCreateWindow(100,100)
glClearColor(0,0,0)
glViewPort(-1, -1, 50, 50)
glClear()
<<<<<<< Updated upstream
glColor(0,1,0)
glVertex(0,0)
=======
glColor(1,0,0)
glLine(-0.6,0.3,-0.3,0)
glLine(-0.6,0,-0.3,-0.4)
glLine(-0.6,0.3,-0.6,0)
glLine(-0.3,0,-0.3,-0.4)
glLine(-0.3,-0.4,0,-0.3)
glLine(0,-0.3,0,-0.15)
glLine(0,-0.15,0.2,-0.06)
glLine(0.2,-0.06, 0.2,-0.25)
glLine(0.2,-0.25,0.5,-0.14)
glLine(0.5,-0.14,0.5, 0.16)
glVertex(0.5,0.16)
glLine(0.5, 0.16,0.1,0.4)
glLine(0.1,0.4,-0.3,0)
glLine(0.1,0.4,-0.3,0.6)
glLine(-0.3,0.6,-0.6,0.3)

#chimenea
glLine(-0.1,0.50,-0.1,0.61)
glLine(-0.04,0.47,-0.04,0.60)
glLine(-0.04,0.60,-0.1,0.61)
glLine(0.05,0.43,0.05,0.6155)
glLine(0.05,0.6155,-0.04,0.60)
glLine(-0.1,0.61,-0.01,0.6195)
glLine(-0.01,0.6195,0.05,0.6150)




>>>>>>> Stashed changes
glFinish()

