n = int(input("Enter number of processes: "))
burst_time = []
arrival_time = []
for i in range(n):
    at = int(input(f"\nEnter Arrival Time for P{i+1}: "))
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    arrival_time.append(at)
    burst_time.append(bt)
# Combine all data into a list of tuples (index, AT, BT)
processes = [(i, arrival_time[i], burst_time[i]) for i in range(n)]
# Sort by arrival time, then burst time
processes.sort(key=lambda x: (x[1], x[2]))
time = 0
completion_time = []
turnaround_time = []
waiting_time = []
for i, at, bt in processes:
    if time < at:
        time = at
    ct = time + bt
    tat = ct - at
    wt = tat - bt
    completion_time.append(ct)
    turnaround_time.append(tat)
    waiting_time.append(wt)
    time = ct
print("\nP\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    idx = processes[i][0]
    print(f"P{idx+1}\t{arrival_time[idx]}\t{burst_time[idx]}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")
