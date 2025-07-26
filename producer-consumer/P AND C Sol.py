# Problem can be solved using Semaphore oncept od synchronization 
import threading
import time
from threading import Semaphore, Lock
buffer = []
buffer_size = 3
empty = Semaphore(buffer_size)
full = Semaphore(0)
mutex = Lock()
def producer():
    for i in range(5):
        empty.acquire()
        mutex.acquire()
        buffer.append(i)
        print(f"Produced: {i}")
        mutex.release()
        full.release()
        time.sleep(1)
def consumer():
    for i in range(5):
        full.acquire()
        mutex.acquire()
        item = buffer.pop(0)
        print(f"Consumed: {item}")
        mutex.release()
        empty.release()
        time.sleep(1.5)
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start()
t2.start()
t1.join()
t2.join()
