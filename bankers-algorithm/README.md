# Banker's Algorithm

##  Description

Banker's Algorithm is a deadlock avoidance algorithm used in operating systems to check whether granting a request leads to a safe state or not.

This project takes:
- Allocation matrix
- Maximum need matrix
- Available resources

And determines if the system is in a **safe state** using the Banker's Algorithm.

---

##  Sample Input
Enter number of processes:  4
Enter number of resource types:  3

Enter Allocation Matrix:

P0:  1 2 3

P1:  4 5 6

P2:  7 8 9

P3:  2 5 8

Enter Max Need Matrix:

P0:  9 8 7 

P1:  7 6 5

P2:  5 4 3

P3:  4 3 2

Enter Available Resources:
 3 2 2

 ## Output
 System is in a safe state.
 
 Safe sequence: P1 -> P2 -> P0 -> P3
