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
        i += 1
    i,j = 0,0
    while i < len(matrix):
        if i in positions["x"]:
            while j < len(matrix[i]):
                matrix[i][j] = 0
                j += 1
        i+=1

    return matrix

print(zeroMatrix([[0,1,2], [1,2,3], [1,2,3]]))