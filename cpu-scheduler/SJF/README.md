# SJF - Shortest Job First (Non-Preemptive)

##  Description
Shortest Job First (SJF) scheduling selects the process with the smallest burst time from the ready queue. In its non-preemptive form, the currently running process is not interrupted.

##  Key Points
- Improves average waiting time
- Non-preemptive (once a process starts, it completes)
- Can lead to starvation of long processes

##  Metrics Calculated
- Completion Time (CT)
- Turnaround Time (TAT)
- Waiting Time (WT)

##  Sample Input
 Enter number of processes:  7

Enter Arrival Time for P1:  1
Enter Burst Time for P1:  4

Enter Arrival Time for P2:  6
Enter Burst Time for P2:  8

Enter Arrival Time for P3:  7
Enter Burst Time for P3:  2

Enter Arrival Time for P4:  7
Enter Burst Time for P4:  3

Enter Arrival Time for P5:  6
Enter Burst Time for P5:  2

Enter Arrival Time for P6:  9
Enter Burst Time for P6:  4

Enter Arrival Time for P7:  2
Enter Burst Time for P7:  3

## Sample Output
P	  AT BT CT TAT WT
P1	1  4	 5	4	 0
P7	2	 3	 8	6  3
P5	6	 2	10	4	  2
P2	6	 8  18  12	4
P3	7	 2	20	13	11
P4	7	 3	23	16	13
P6	9	 4	27	18	14

