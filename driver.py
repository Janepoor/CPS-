#COMS 4701
#Auther: Jianpu Ma jm4437


from  sudokus import sudokusCSP,Sudoku
import sys


try:
    sudokus= sys.argv[1]
except IndexError as e:
    print e
    print ("The input requires a string indicating a sudoku board")



board = sudokusCSP(sudokus)

x = BacktrackingSearch(board)

for var in x:
    board.domain[var] = [x[var]]


sol = ""
for row in xrange(65,74):
    for col in xrange(1,10):
        sol += str(board.domain[chr(row) + str(col)][0])

    with open("output.txt", "w") as output:
        output.write(sol)