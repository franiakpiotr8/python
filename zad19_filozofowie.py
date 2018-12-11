# !python

import threading
import time

#forks 0 == dirty, 1 == clean
forks = [0, 0, 0, 0, 0]

#fork_owner ID of current fork owner
fork_owner = [0, 1, 2, 3, 4]

#fork_requested - 0 == nobody reqested that fork, 1 == someone requested fork
fork_requested = [0, 0, 0, 0, 0]

#eating - 0 == philosopher finished eating, 1==philosopher still eats
eating = [1, 1, 1, 1, 1]


def eat(my_ID):
    obtained_forks = 0

    while eating[my_ID]:

        if not(fork_owner[my_ID] == my_ID):
            fork_requested[my_ID] = 1

        if not (fork_owner[(my_ID+1) % 5] == my_ID):
            fork_requested[(my_ID+1) % 5] = 1

        if fork_owner[my_ID] == 5 and fork_requested[my_ID] == 1:
            fork_owner[my_ID] = my_ID
            fork_requested[my_ID] = 0
            obtained_forks = obtained_forks + 1
            print("Filozof nr " + str(my_ID) + " otrzymał widelec")

        if fork_owner[(my_ID+1) % 5] == 5 and fork_requested[(my_ID+1) % 5] == 1:
            fork_owner[(my_ID+1) % 5] = my_ID
            fork_requested[(my_ID+1) % 5] = 0
            obtained_forks = obtained_forks + 1
            print("Filozof nr " + str(my_ID) + " otrzymał widelec")

        for fork_id in range(len(forks)):
            if fork_owner[fork_id] == my_ID:
                if fork_requested[fork_id] == 1 and forks[fork_id] == 0:
                    forks[fork_id] = 1
                    fork_owner[fork_id] = 5
                    print("Filozof nr " + str(my_ID) + " umył i oddał widelec")

        if fork_owner.count(my_ID) == 2:
            if forks[my_ID] == 1 and forks[(my_ID+1) % 5] == 1:
                time.sleep(2)
                obtained_forks = 0
                fork_owner[my_ID] = 5
                fork_owner[(my_ID+1) % 5] = 5
                forks[my_ID] = 1
                forks[(my_ID+1) % 5] = 1
                eating[my_ID] = 0
                print("Filozof nr " + str(my_ID) + " zjadł. Umył i oddał 2 widelce")
        time.sleep(1)


print(forks)
thread1 = threading.Thread(target=eat, name="filozof 0", args=[0])
thread2 = threading.Thread(target=eat, name="filozof 1", args=[1])
thread3 = threading.Thread(target=eat, name="filozof 2", args=[2])
thread4 = threading.Thread(target=eat, name="filozof 3", args=[3])
thread5 = threading.Thread(target=eat, name="filozof 4", args=[4])

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

print("Success " + str(eating))
