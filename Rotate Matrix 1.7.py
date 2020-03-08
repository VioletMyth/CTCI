import copy
def rotateMatrix(matrix):
    copyMatrix = copy.deepcopy(matrix)
    i,j,l = 0,0,0
    k = len(matrix) - 1
    while i < len(matrix):
        while j < len(matrix[i]):
            matrix[i][j] = copyMatrix[k][l]
            k -= 1
            j += 1
        i += 1
        l += 1
    return matrix

print(rotateMatrix([[1,2,3],[1,2,3], [1,2,3]]))
