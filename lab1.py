from gl import *
from render import *

primerP=[[165, 380],[185, 360] ,[180, 330] ,[207, 345] ,[233, 330], [230, 360] ,[250, 380] ,[220, 385] ,[205, 410] ,[193, 383]]
segundoP= [[321, 335], [288, 286], [339, 251] ,[374, 302]]
tercerP=[[377, 249], [411, 197], [436, 249]]
cuartoP=[[413, 177], [448, 159], [502, 88], [553, 53], [535, 36], [676, 37], [660, 52],[750, 145], [761, 179], [672, 192], [659, 214], [615, 214], [632, 230], [580, 230],[597, 215], [552, 214], [517, 144], [466, 180]]
quintoP=[[682, 175], [708, 120], [735, 148], [739, 170]]
glInit()
glCreateWindow(800,800)
glClearColor(0,0,0)
glClear()
glColor(1,1,1)

glDelineado(primerP)
glColoreado(primerP)
glDelineado(segundoP)
glColoreado(segundoP)
glDelineado(tercerP)
glColoreado(tercerP)
glDelineado(cuartoP)
glColoreado(cuartoP)
glDelineado(quintoP)
glColor(0,0,0)
glColoreado(quintoP)







glFinish()