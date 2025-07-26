# FCFS - First Come First Serve

##  Description
The First Come First Serve (FCFS) scheduling algorithm executes processes in the order they arrive. It is non-preemptive, meaning once a process starts, it runs to completion.

##  Key Points
- Simple and easy to implement
- Non-preemptive
- High average waiting time if shorter processes arrive later

##  Metrics Calculated
- Completion Time (CT)
- Turnaround Time (TAT)
- Waiting Time (WT)

##  Sample Input
Enter number of processes:  5
Enter arrival time for Process P1:  0
Enter burst time for Process P1:  5
Enter arrival time for Process P2:  1
Enter burst time for Process P2:  7
Enter arrival time for Process P3:  2
Enter burst time for Process P3:  8
Enter arrival time for Process P4:  4
Enter burst time for Process P4:  6
Enter arrival time for Process P5:  5
Enter burst time for Process P5:  8

## Sample Output
PID	AT	BT	CT	TAT	WT
P1	0	5	5	5	0
P2	1	7	12	11	4
P3	2	8	20	18	10
P4	4	6	26	22	16
P5	5	8	34	29	21


