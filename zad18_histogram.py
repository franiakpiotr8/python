# !python

import threading
import random

def calculate_hist(data, hist_data):
    for elem in data:
        hist_data[elem] = hist_data[elem] + 1


data = list()
hist_data = list()
for i in range(10):
    hist_data.append(0)

for i in range(100):
    data.append(random.randrange(10))

thread1 = threading.Thread(target=calculate_hist, name="Hist 1", args=(data[0:50], hist_data))
thread2 = threading.Thread(target=calculate_hist, name="Hist 2", args=(data[50:len(data)], hist_data))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

for i in range(len(hist_data)):
    print(str(i) + "| ", end='')
    for k in range(hist_data[i]):
        print("*", end='')
    print("")
