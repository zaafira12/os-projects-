def is_safe(processes, available, max_need, allocation):
    n = len(processes)
    m = len(available)
    # Calculate Need matrix
    need = [[max_need[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]
    # Initialize finish flags and safe sequence
    finish = [False] * n
    safe_seq = []
    work = available.copy()
    while len(safe_seq) < n:
        found = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                # Process i can be executed
                for j in range(m):
                    work[j] += allocation[i][j]
                finish[i] = True
                safe_seq.append(i)
                found = True
                break
        if not found:
            return False, []

    return True, safe_seq
# User Input
n = int(input("Enter number of processes: "))
m = int(input("Enter number of resource types: "))
processes = list(range(n))
print("\nEnter Allocation Matrix:")
allocation = [list(map(int, input(f"P{i}: ").split())) for i in range(n)]
print("\nEnter Max Need Matrix:")
max_need = [list(map(int, input(f"P{i}: ").split())) for i in range(n)]
print("\nEnter Available Resources:")
available = list(map(int, input().split()))
# Check if system is in safe state
safe, sequence = is_safe(processes, available, max_need, allocation)
if safe:
    print("\nSystem is in a safe state.")
    print("Safe sequence:", ' -> '.join(f"P{p}" for p in sequence))
else:
    print("\nSystem is NOT in a safe state.")