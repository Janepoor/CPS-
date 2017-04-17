#COMS 4701
#Auther: Jianpu Ma jm4437





class Sudoku():

    def __init__(self,board):
        self.board={}
        self.remain=[]
        self.n=9
        i=0
        for row in range(65,74):
            for colum in range(1,9):
                self.board[chr(row)+str(colum)]=int(board[i])
                if self.board[i]==0:
                    self.remain.append(chr(row)+str(colum))
                i+=1



    def getblank(self):
        return list(self.remain)

    def getvalue(self,sign):
        return self.board[sign]

    def setvalue(self,sign,value):
        if value.isint:
            self.board[sign]=value
        else:
            print("Value must be int")

    


