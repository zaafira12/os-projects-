#  FIFO Page Replacement Algorithm
This folder contains a Python implementation of the **FIFO (First-In, First-Out)** page replacement algorithm with user input and memory simulation.

---

##  What is FIFO?
**FIFO (First-In, First-Out)** is a basic page replacement algorithm used in Operating Systems. It replaces the **oldest page** in memory when a new page needs to be loaded and no space is available.

> It’s simple but may not always perform well for real-world workloads.

---

##  Working Logic

1. Pages are stored in a queue.
2. When a new page arrives:
   - If there is space, it is added to memory.
   - If memory is full:
     - The page that entered **first** is removed (dequeued).
     - The new page is added (enqueued).
3. Hits and faults are tracked based on whether the page is already in memory.

---

##  Input Format

- **Page Reference String**: Space-separated integers
- **Number of Frames**: Integer

Example:

Enter page reference string (space-separated):  1 2 3 4 5 5 4 3 2 1

Enter number of frames:  3


---

##  Output Example

--- FIFO Page Replacement ---

Page: 1 => Memory: [1]

Page: 2 => Memory: [1, 2]

Page: 3 => Memory: [1, 2, 3]

Page: 4 => Memory: [2, 3, 4]

Page: 5 => Memory: [3, 4, 5]

Page: 5 => Memory: [3, 4, 5] (Hit)

Page: 4 => Memory: [3, 4, 5] (Hit)

Page: 3 => Memory: [3, 4, 5] (Hit)

Page: 2 => Memory: [4, 5, 2]

Page: 1 => Memory: [5, 2, 1]

Total Page Faults: 7

Total Page Hits  : 3
