# Round Robin CPU Scheduling
n = int(input("Enter number of processes: "))
bt = []  # Burst Time
at = []  # Arrival Time
for i in range(n):
    at.append(int(input(f"\nEnter Arrival Time for P{i+1}: ")))
    bt.append(int(input(f"Enter Burst Time for P{i+1}: ")))
quantum = int(input("\nEnter Time Quantum: "))
# Initialize
rem_bt = bt.copy()      # Remaining burst times
ct = [0]*n              # Completion times
wt = [0]*n              # Waiting times
tat = [0]*n             # Turnaround times
time = 0
queue = []
visited = [False]*n
# Start with processes that arrive at time 0
for i in range(n):
    if at[i] <= time and not visited[i]:
        queue.append(i)
        visited[i] = True
while queue:
    i = queue.pop(0)
    if rem_bt[i] > quantum:
        time += quantum
        rem_bt[i] -= quantum
    else:
        time += rem_bt[i]
        ct[i] = time
        rem_bt[i] = 0
    # Enqueue new processes that have arrived
    for j in range(n):
        if at[j] <= time and not visited[j] and rem_bt[j] > 0:
            queue.append(j)
            visited[j] = True
    # If current process still has time left, re-add it
    if rem_bt[i] > 0:
        queue.append(i)
# Calculate TAT and WT
for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]
# Output
print("\nP\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"P{i+1}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
