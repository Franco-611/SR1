class MAT(object):
    def __init__(self, mat): 
        self.mat = mat

    def __add__(self, other):
        temp = [[ 0 for y in range(len(self.mat))]
                    for x in range(len(self.mat))]
        
        try:
            for y in range(len(temp)):
                for x in range(len(temp[y])):
                    temp[x][y] = self.mat[x][y] + other.mat[x][y]

            return temp

        except:
            print ("Suma no valida")

    def __sub__(self, other):
        temp = [[ 0 for y in range(len(self.mat))]
                    for x in range(len(self.mat))]
        try:
            for y in range(len(self.mat)):
                for x in range(len(self.mat[y])):
                    temp[x][y] = self.mat[x][y] - other.mat[x][y]

            return temp

        except:
            print ("Resta no valida")

    def __mul__(self, other):

        temp = [[ 0 for y in range(len(self.mat))]
                    for x in range(len(self.mat))]

        for x in range(len(self.mat)) :
            for y in range(len(other.mat[0])):
                total = 0
                for f in range(len(other.mat)):
                    total += self.mat[x][f] * other.mat[f][y]
                temp[x][y]+= total

        return temp

    

                

                    
