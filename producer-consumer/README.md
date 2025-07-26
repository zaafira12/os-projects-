# Producer-Consumer Problem (OS Project)

This project demonstrates the classic **Producer-Consumer Problem** using Python, with two versions:

- `solution.py` – With **Semaphore and Lock synchronization**
- `problem.py` – Without synchronization to show the issue

---

##  Problem Statement
In operating systems, the **Producer-Consumer problem** is a classic example of a multi-process synchronization issue. It involves two processes:

- **Producer** – Produces data and adds it to a shared buffer
- **Consumer** – Consumes data from that shared buffer

They must be synchronized so:
- The **producer doesn’t add data** when the buffer is full
- The **consumer doesn’t remove data** when the buffer is empty

---

##  `problem.py` – Without Synchronization

This version does not use any synchronization mechanism like semaphores or locks.

###  Key Issues Shown:

- The **producer keeps producing** even if the buffer is full
- The **consumer may try to consume** from an empty buffer
- No mutual exclusion → race conditions

### Output Example:
Produced: 0 | Buffer: [0]

Consumed: 0 | Buffer: []

Produced: 1 | Buffer: [1]

Consumed: 1 | Buffer: []

Produced: 2 | Buffer: [2]

Produced: 3 | Buffer: [2, 3]

Consumed: 2 | Buffer: [3]

Produced: 4 | Buffer: [3, 4]

Consumed: 3 | Buffer: [4]

Produced: 5 | Buffer: [4, 5]

Produced: 6 | Buffer: [4, 5, 6]

Consumed: 4 | Buffer: [5, 6]

Produced: 7 | Buffer: [5, 6, 7]

Consumed: 5 | Buffer: [6, 7]

Produced: 8 | Buffer: [6, 7, 8]

Buffer full! Producer is waiting...

Consumed: 6 | Buffer: [7, 8]

Consumed: 7 | Buffer: [8]

Consumed: 8 | Buffer: []

Buffer empty! Consumer is waiting...


---

## `solution.py` – With Semaphore & Lock

This version solves the problem using:

- **Semaphores**: `empty` and `full`
- **Mutex Lock**: For mutual exclusion while accessing the buffer

###  Synchronization Logic:

- `empty.acquire()` → Producer waits if buffer is full
- `full.acquire()` → Consumer waits if buffer is empty
- `mutex.acquire()` → Only one thread accesses buffer at a time

###  Sample Output:
Produced: 0

Consumed: 0

Produced: 1

Consumed: 1

Produced: 2

Produced: 3

Consumed: 2

Produced: 4

Consumed: 3

Consumed: 4

##  Concepts Used

- Threads (`threading.Thread`)
- **Semaphores** for signaling between threads
- **Lock** for mutual exclusion
- Shared buffer
- Real-time thread simulation with `time.sleep()`

---


