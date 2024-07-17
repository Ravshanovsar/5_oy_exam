import threading
import time
def numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)

def letters():
    for i in ("A", "B", "C", "D", "E"):
        print(i)
        time.sleep(1)

thread1 = threading.Thread(target=numbers)
thread2 = threading.Thread(target=letters)

thread1.start()
thread2.start()
thread2.join()