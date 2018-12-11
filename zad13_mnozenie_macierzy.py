# !python


import random

print("==========zadanie13==========")
matrix1 = [[random.randrange(10) for i in range(8)] for i in range(8)]
matrix2 = [[random.randrange(10) for i in range(8)] for i in range(8)]
result_matrix = [[0 for i in range(8)] for i in range(8)]

for i in range(8):
    for j in range(8):
        for k in range(8):
            result_matrix[i][j] = result_matrix[i][j] + matrix1[i][k] * matrix2[k][j]

for i in range(8):
    print(matrix1[i])
print("\n")
for i in range(8):
    print(matrix2[i])
print("\n")
for i in range(8):
    print(result_matrix[i])
