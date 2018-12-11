# !python
import os
print("==========zadanie3==========")
path = input("Wprowadz siezke do katalogu: ")


object = os.scandir(path)
dir_num = 0
for iterator in object:
    if iterator.is_dir():
        dir_num = dir_num + 1
        print(iterator.name)

print("Liczba katalogów: " + str(dir_num))