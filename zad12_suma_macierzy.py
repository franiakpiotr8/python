# !python

import random

print("==========zadanie12==========")

matrix1 = [[random.randrange(100) for i in range(128)] for i in range(128)]
matrix2 = [[random.randrange(100) for i in range(128)] for i in range(128)]
result_matrix = [[0 for i in range(128)] for i in range(128)]

for i in range(128):
    for j in range(128):
        result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

for i in range(128):
    print(matrix1[i])

print("\n")
for i in range(128):
    print(matrix2[i])
print("\n")
for i in range(128):
    print(result_matrix[i])
