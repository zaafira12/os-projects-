#  FCFS Page Replacement Algorithm
This project implements the **FCFS (First-Come, First-Served)** page replacement algorithm in Python with user input.

---

##  Problem Statement

In **memory management**, FCFS is one of the simplest page replacement techniques. When a page needs to be replaced, the **oldest loaded page (the one that came first)** is removed from memory.

- No priority is given to recently or frequently used pages.
- Simple queue-based structure.

---

##  User Input Format

- A **space-separated list** of page numbers (reference string)
- The **number of available frames**

---

##  How It Works

1. Pages are loaded one by one.
2. If a page is **not already in memory**, it is loaded (page fault).
3. If the memory is **full**, the page that was loaded **first** (oldest) is replaced.
4. If the page is already in memory, it is a **page hit**.

---

##  Example

###  Input
 Enter page reference string (space-separated):  1 3 5 8 0 2 4 1 3 5 8 9 
 Enter number of frames:  3

### Output
Page: 1 => Memory: [1]

Page: 3 => Memory: [1, 3]

Page: 5 => Memory: [1, 3, 5]

Page: 8 => Memory: [3, 5, 8]

Page: 0 => Memory: [5, 8, 0]

Page: 2 => Memory: [8, 0, 2]

Page: 4 => Memory: [0, 2, 4]

Page: 1 => Memory: [2, 4, 1]

Page: 3 => Memory: [4, 1, 3]

Page: 5 => Memory: [1, 3, 5]

Page: 8 => Memory: [3, 5, 8]

Page: 9 => Memory: [5, 8, 9]

Page Faults: 12

Page Hits  : 0

