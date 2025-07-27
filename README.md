#  Operating System Projects

This repository contains **well-structured Python implementations** of core concepts in **Operating Systems**, including:

- CPU Scheduling Algorithms  
- Page Replacement Strategies  
- Banker's Algorithm (Deadlock Avoidance)  
- Producer-Consumer Problem (Synchronization)

Each project is organized into its own folder with:
-  Python Code
- User Input Support
-  Step-by-Step Output
- README File

---

##  Topics Covered

### 1.  CPU Scheduling Algorithms

Simulates how an OS schedules processes for execution on the CPU. Includes:

| Algorithm       | Description                                  | Link        |
|----------------|----------------------------------------------|-------------|
| FCFS            | First-Come, First-Served (non-preemptive)    | [View](cpu-scheduler/FCFS) |
| SJF             | Shortest Job First (non-preemptive)          | [View](cpu-scheduler/SJF)  |
| Round Robin     | Time-slice based preemptive scheduling       | [View](cpu-scheduler/RoundRobin) |

 **Input:** Process burst times, arrival times (optional), and quantum (for RR)  
 **Output:** Gantt Chart, Waiting Time, Turnaround Time  

---

### 2.  Page Replacement Algorithms

Manages how pages are loaded into memory when frames are full. Includes:

| Algorithm | Description                                       | Link         |
|-----------|---------------------------------------------------|--------------|
| FIFO      | Replaces the oldest page in memory                | [View](page-replacement/Fifo) |
| FCFS      | Similar to FIFO, kept for scheduling-style view   | [View](page-replacement/fcfs) |
| LRU       | Removes the least recently used page              | [View](page-replacement/LRU)  |

 **Input:** Reference string, number of frames  
 **Output:** Page hits, page faults, memory status

---

### 3. Banker's Algorithm (Deadlock Avoidance)

Implements the classic **Banker's Algorithm** used for **safe state checking** in deadlock avoidance.

- Checks whether a resource allocation is safe
- Accepts input for available resources, allocation, and maximum need
- Calculates **Need Matrix** and performs **Safety Check**

 [View Project](bankers-algorithm)

---

### 4. 🔁 Producer-Consumer Problem (With Semaphores)
Classic **process synchronization problem**, demonstrating inter-process communication using a **bounded buffer**.


| Part     | Description                                                                     |
|----------|---------------------------------------------------------------------------------|
| Problem  | Simulates producer waiting when buffer is full, and consumer when empty         |
| Solution | Uses Semaphore logic to synchronize producer and consumer actions               |

 [View Project](producer-consumer)

---

##  Folder Structure

os-project/

├── cpu-scheduling/

│ ├── fcfs/

│ ├── sjf/

│ └── roundrobin/

├── page-replacement/

│ ├── fifo/

│ ├── fcfs/

│ └── lru/

├── bankers-algorithm/

├── producer-consumer/

│ ├── problem/

│ └── solution/

└── README.md 
