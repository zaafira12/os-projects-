#  Page Replacement Algorithms 

This repository contains Python implementations of the **most common Page Replacement Algorithms** used in Operating Systems to manage memory effectively.

---

##  What is Page Replacement?

Page replacement algorithms are used in **virtual memory systems** when a page of memory needs to be loaded but the available frames are full. These algorithms decide **which page to replace** to make room for the new one.

---

##  Algorithms Implemented

Each algorithm has its own folder with:

-  Python code
- User input support
-  Page fault and hit tracking
-  Code explanation
-  Individual README

###  1. FIFO – First-Come, First-Served
- Removes the **oldest loaded** page first.
- Simple but can result in more faults.
- [Go to FIFO →](./Fifo)

### 🔹 2. LRU – Least Recently Used
- Removes the page that **hasn’t been used for the longest time**.
- Smarter than FIFO.
- [Go to LRU →](./LRU)

### 🔹 3. FCFS 
- A special folder to test FCFS logic in a scheduling-style view.
- [Go to FCFS →](./fcfs)

---





