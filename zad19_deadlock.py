# !python

import threading
import time

#deadlock
forks = [0, 0, 0, 0, 0]


def eat(id_num):
    forks_num = 0
    for i in range(len(forks)):
        if 0 == forks[i] and forks_num < 2:
            forks[i] = 1
            forks_num = forks_num + 1
            print("Filozof nr " + str(id_num) + " dostał widelec")
            time.sleep(2)
        if forks_num < 2:
            print("Filozof nr " + str(id_num) + " ma " + str(forks_num) + " widelec. Czeka na kolejny")
        else:
            print("Filozof nr " + str(id_num) + " je . Ma " + str(forks_num))


thread1 = threading.Thread(target=eat, name="filozof 1", args=[1])
thread2 = threading.Thread(target=eat, name="filozof 2", args=[2])
thread3 = threading.Thread(target=eat, name="filozof 3", args=[3])
thread4 = threading.Thread(target=eat, name="filozof 4", args=[4])
thread5 = threading.Thread(target=eat, name="filozof 5", args=[5])

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
