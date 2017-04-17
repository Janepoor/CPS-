#COMS 4701
#Auther: Jianpu Ma jm4437


class Sudoku():

    def __init__(self,board):
        self.board={}
        self.remain=[]
        self.n=9


        #### Initialize with value
        i=0
        for row in range(65,74):
            for colum in range(1,10):
                self.board[chr(row)+str(colum)]=int(board[i])
                if self.board[i]==0:
                    self.remain.append(chr(row)+str(colum))
                i+=1


    def getblank(self):
        return list(self.remain)

    def getvalue(self,sign):
        return self.board[sign]

    def getkeys(self):
        return self.board.keys()

    def setvalue(self,sign,value):
        if value.isint:
            self.board[sign]=value
        else:
            print("Value must be int")



class sudokusCSP(CSP):
    """
    Class representing the sudoku CSP:
    - Variables: Rows are named from A-I, columns are named from 1-9 and variable names from A1, to I9
    - Domain: Each variable can take values from 1-9
    - Constraints: Sudoku's constraints
    """

    def __init__(self,sudoku):
        self.sudoku=sudoku
        self.variable=sudoku.keys()
        self.remain=sudoku.getblank()



        ## Setting domain
        self.domain={}
        for v in self.variable:
            if self.sudoku.getvalue():
                self.domain[v]=[self.sudoku.getvalue()]
            else:
                self.domain[v]=[1,2,3,4,5,6,7,8,9]



        ## Setting Constrain
        self.constrain=[]
        ###Adding row constraint
        self.constrain=[]
        rowlist=[]
        for row in range(65,74):
            for colum in range(1,10):
                rowlist.append(chr(row)+str(colum))
            self.constrain.append(rowlist)  #["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9]"

        ###Adding colum constraint
        columlist=[]
        for colum in range(1,10):
            for row in range(65,74):
                columlist.append(chr(row)+str(colum))
            self.constrain.append(rowlist)  #"[A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1]"


        ###Add Square constraint  "A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        row_start = 65
        while (row_start < 74):
            colum_start = 1
            while (colum_start < 10):
                squarelsit = []
                for row in range(row_start, row_start + 3):
                    for colum in range(colum_start, colum_start + 3):
                        squarelsit.append(chr(row) + str(colum))
                self.constrain.append(squarelsit)
                colum_start += 3
            row_start += 3


        #### Add Binary constrain n

        self.binary_constraints = []
        for cell in self.variables:
            for constraint in self.constraints:
                if cell in constraint:
                    for otherCell in constraint:
                        if otherCell != cell:
                            self.binary_constraints.append((cell, otherCell))




    def getneighbor(self,x,restriction=None):
        neighbor=[]
        for arc in self.binary_constraints:
            if x==arc[0]:
                if restriction:
                    if restriction!=arc[1]:
                        neighbor.append(arc[1])
                    else:
                        neighbor.append(arc[1])
        return neighbor




    def check(self,variables):

        for constrain in self.constrain:

            for i in xrange(81):
                if self.sudoku.getvalue(constrain[i]):
                    for j in xrange(i + 1, 81):
                        if self.sudoku.getvalue(constrain[j]):
                            if self.sudoku.getvalue(constrain[i]) == self.sudoku.getvalue(constrain[j]):
                                return False

        return True



def main():

    pass

if __name__ == '__main__':
    main()

