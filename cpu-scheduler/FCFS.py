# fcfs.py
def fcfs(processes):
    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    time = 0
    print("\nPID\tAT\tBT\tCT\tTAT\tWT")
    for pid, at, bt in processes:
        time = max(time, at)
        ct = time + bt
        tat = ct - at
        wt = tat - bt
        print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")
        time = ct

# Get user input
n = int(input("Enter number of processes: "))
processes = []

for i in range(n):
    at = int(input(f"Enter arrival time for Process P{i+1}: "))
    bt = int(input(f"Enter burst time for Process P{i+1}: "))
    processes.append([f"P{i+1}", at, bt])

fcfs(processes)
