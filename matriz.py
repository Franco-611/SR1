class MAT(object):
    def __init__(self, mat): 
        self.mat = mat

    def __add__(self, other):

        temp = []
        for i in range(len(self.mat)):
            temp.append([])
            for j in range(len(self.mat[i])):
                temp[i][j].append(0)
        
        try:
            for y in range(len(temp)):
                for x in range(len(temp[y])):
                    temp[x][y] = self.mat[x][y] + other.mat[x][y]

            return temp

        except:
            print ("Suma no valida")

    def __sub__(self, other):
        try:
            for y in range(len(self.mat)):
                for x in range(len(self.mat[y])):
                    self.mat[x][y] -= other.mat[x][y]

            return self.mat

        except:
            print ("Resta no valida")
    

                

                    
