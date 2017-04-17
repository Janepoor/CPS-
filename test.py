

"""constrain=[]
row_start = 65
colum_start = 1

while (colum_start < 10):
    squarelsit = []
    for row in range(row_start, row_start + 3):
        for colum in range(colum_start, colum_start + 3):
            squarelsit.append(chr(row) + str(colum))
    constrain.append(squarelsit)
    colum_start += 3

row_start=68
colum_start=1

while (colum_start<10):
    squarelsit = []
    for row in range(row_start, row_start + 3):
        for colum in range(colum_start, colum_start + 3):
            squarelsit.append(chr(row) + str(colum))
    constrain.append(squarelsit)
    colum_start+=3

row_start=71
colum_start=1

while (colum_start<10):
    squarelsit = []
    for row in range(row_start, row_start + 3):
        for colum in range(colum_start, colum_start + 3):
            squarelsit.append(chr(row) + str(colum))
    constrain.append(squarelsit)
    colum_start+=3"""



constrain=[]
row_start = 65

while(row_start<74):
    colum_start = 1
    while (colum_start < 10):
        squarelsit = []
        for row in range(row_start, row_start + 3):
            for colum in range(colum_start, colum_start + 3):
                squarelsit.append(chr(row) + str(colum))
        constrain.append(squarelsit)
        colum_start += 3
    row_start+=3


print(constrain)

