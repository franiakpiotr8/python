# !python

import random


def det(matrix):
    if len(matrix) == len(matrix[0]):
        width = len(matrix[0])
        if width == 1:
            return matrix[0][0]
        else:
            sum = 0
            for i in range(width):
                sign = pow(-1, 2 + i)
                temp_buff = []
                for j in range(0, width-1):
                    temp_buff.append([])
                    for k in range(width):
                        if k != i:
                            temp_buff[j].append(matrix[j+1][k])
                sum += sign * det(temp_buff) * matrix[0][i]
            return sum


size = 5
test_matrix = [[random.randrange(10) for i in range(size)] for j in range(size)]
print(test_matrix)
det_matrix = det(test_matrix)
print(det_matrix)
