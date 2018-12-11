# !python

print("==========zadanie11==========")


a = [1, 2, 12, 4]
b = [2, 4, 2, 8]
result = 0
for x in range(0, len(a)):
    result = result + a[x]*b[x]

print(result)
