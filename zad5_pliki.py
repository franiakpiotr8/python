# !python
import os
print("==========zadanie5==========")

def find_dir(path):
    object = os.scandir(path)
    for iterator in object:
        if iterator.is_file():
            print(iterator.name)
        else:
            find_dir(iterator.path)

path = input("Wprowadz siezke do katalogu: ")
find_dir(path)
