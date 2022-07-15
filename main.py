from gl import *

glInit()
glCreateWindow(100,100)
glClearColor(0,0,0)
glViewPort(-1, -1, 50, 50)
glClear()
glColor(0,1,0)
glVertex(0,0)
glFinish()

