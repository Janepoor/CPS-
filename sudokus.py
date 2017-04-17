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

        row_start=65
        colum_start=1

        while(colum_start<=10):
            squarelsit = []
            for row in range(row_start,row_start+3):
                for colum in range(colum_start,colum_start+3):
                    squarelsit.append(chr(row)+str(colum))
            self.constrain.append(squarelsit)
            row_start+=3
            colum_start+=3







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




