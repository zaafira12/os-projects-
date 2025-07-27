def fifo(pages, capacity):
    memory = []
    page_faults = 0
    page_hits = 0

    for page in pages:
        if page in memory:
            page_hits += 1
        else:
            page_faults += 1
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
        print(f"Page: {page} => Memory: {memory}")

    print(f"\nPage Faults: {page_faults}")
    print(f"Page Hits  : {page_hits}")

# User input
pages = list(map(int, input("Enter page reference string (space-separated): ").split()))
capacity = int(input("Enter number of frames: "))
fifo(pages, capacity)
