import numpy as np

# Set up matrix 
a = np.array([[1,2,0],[4,0,7],[9,2,1]])
print('Matrix =\n', a, "\n")

# Finding the index positions of all the zeros in the array 
pos = np.where(a == 0)

# Ensure all the rows and columns to be set to zero is unique (creating a set)
x = np.unique(pos[0])
y = np.unique(pos[1])
print("Rows: ", x, "Columns: ", y, "\n")

# Turn each row into row vector of 0s
for row in x:
    a[row, :] = 0

# Turn each column into column vector of 0s
for col in y:
    a[:, col] = 0

print("Result:\n", a)