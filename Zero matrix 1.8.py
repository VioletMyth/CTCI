def zeroMatrix(matrix):
    positions = {"x": [], "y": []}
    i,j = 0,0
    while i < len(matrix):
        if 0 in matrix[i]:
            positions["x"].append(i)
        while j < len(matrix[i]):
            if matrix[i][j] == 0 and j not in positions["y"]:
                positions["y"].append(j)
            
            j += 1
        j = 0
        i += 1
    i,j = 0,0
    while i < len(matrix):
        while j < len(matrix[i]):
            if i in positions["x"]:
                matrix[i][j] = 0
            j += 1
        j = 0
        i+=1
    
    row,column = 0,0
    while column < len(matrix[row]):
        while row < len(matrix):
            if column in positions["y"]:
                matrix[row][column] = 0
            row += 1
        row = 0
        column += 1

    return matrix

print(zeroMatrix([[0,1,1], [1,2,1], [2,3,1], [2,0,1]]))