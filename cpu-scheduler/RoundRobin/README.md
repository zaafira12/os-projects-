# Round Robin Scheduling

##  Description
Round Robin scheduling assigns a fixed time slice (quantum) to each process in a cyclic order. It is preemptive and ensures fair CPU allocation among all processes.

##  Key Points
- Preemptive
- Time-sharing system
- Fair, avoids starvation
- Depends heavily on time quantum value

##  Time Quantum
You must specify a time quantum (e.g., 2 units).

##  Metrics Calculated
- Completion Time (CT)
- Turnaround Time (TAT)
- Waiting Time (WT)

##  Sample Input
Enter number of processes:  4

Enter Arrival Time for P1:  0
Enter Burst Time for P1:  3

Enter Arrival Time for P2:  1
Enter Burst Time for P2:  6

Enter Arrival Time for P3:  3
Enter Burst Time for P3:  7

Enter Arrival Time for P4:  5
Enter Burst Time for P4:  7

Enter Time Quantum:  2

## Sample Output
P	AT	BT	CT	TAT	WT

P1	0	3	5	5	2

P2	1	6	15	14	8

P3	3	7	22	19	12

P4	5	7	23	18	11


