# !python

import os


print("==========zadanie6==========")

# utworzenie plików .jpg

for i in range(4):
    file = open("file_" + str(i) + ".jpg", 'w+')
    file.close()

for i in range(4):
    try:
        os.rename("file_" + str(i) + ".jpg", "file_" + str(i)+".png")
    except FileExistsError:
        os.remove("file_" + str(i)+".png")
        os.rename("file_" + str(i) + ".jpg", "file_" + str(i) + ".png")


