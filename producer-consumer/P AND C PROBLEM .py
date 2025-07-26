import threading
import time
buffer = []
buffer_size = 3
def producer():
    for i in range(10):
        if len(buffer) < buffer_size:
            buffer.append(i)
            print(f"Produced: {i} | Buffer: {buffer}")
        else:
            print("Buffer full! Producer is waiting...")
        time.sleep(1)
def consumer():
    for i in range(10):
        if buffer:
            item = buffer.pop(0)
            print(f"Consumed: {item} | Buffer: {buffer}")
        else:
            print("Buffer empty! Consumer is waiting...")
        time.sleep(1.5)
# Create and start threads
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start()
t2.start()
t1.join()
t2.join()
