# LRU Page Replacement Algorithm

This folder contains a Python implementation of the **LRU (Least Recently Used)** page replacement algorithm with user input, page fault, and hit tracking.

---

##  Problem Statement

In virtual memory management, the **LRU algorithm** replaces the page that **has not been used for the longest time**. It is a more efficient strategy than FCFS because it considers recent page usage patterns.

---

##  Key Concept

- Maintain the order of page usage.
- If a page is accessed, it becomes the **most recently used**.
- When replacement is needed, **the least recently used page is removed**.

---

##  Example

###  Input:
Enter page reference string (space-separated):  1 3 5 7 9 9 7 5 3 1

Enter number of frames:  2

### Output
Page: 1 => Memory: [1]

Page: 3 => Memory: [1, 3]

Page: 5 => Memory: [3, 5]

Page: 7 => Memory: [5, 7]

Page: 9 => Memory: [7, 9]

Page: 9 => Memory: [7, 9]

Page: 7 => Memory: [9, 7]

Page: 5 => Memory: [7, 5]

Page: 3 => Memory: [5, 3]

Page: 1 => Memory: [3, 1]

Page Faults: 8

Page Hits  : 2


---

##  How It Works

- Use a list (`memory[]`) to track pages in use.
- When a page is accessed:
  - If it exists → move it to the end (most recently used).
  - If not → remove the first page (least recently used) if full, then add the new page.
- Count and print page faults and hits.

---


