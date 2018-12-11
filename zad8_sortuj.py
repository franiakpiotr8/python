# !python

import random


print("==========zadanie8==========")


def sort(table):
    sorting_finished = False
    temp_val = 0
    while sorting_finished == False:
        sorting_finished = True
        for num in range(0, len(table)-1):
            if table[num] > table[num+1]:
                temp_val = table[num]
                table[num] = table[num+1]
                table[num+1] = temp_val
                sorting_finished = False
    return sorting_finished


values = list()
for x in range(0, 50):
    values.append(random.randint(0, 200))

print("Losowe wartosci: " + str(values))
sort(values)
print("Wynik działania sortowania: " + str(values))
values.sort()
print("Wynik kontrolny           : " + str(values))
