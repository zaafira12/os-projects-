def fifo_page_replacement(pages, frames_count):
    memory = []
    page_faults = 0
    page_hits = 0

    print("\n--- FIFO Page Replacement ---\n")
    for page in pages:
        if page in memory:
            page_hits += 1
            print(f"Page: {page} => Memory: {memory} (Hit)")
        else:
            page_faults += 1
            if len(memory) < frames_count:
                memory.append(page)
            else:
                memory.pop(0)  # Remove the oldest page
                memory.append(page)
            print(f"Page: {page} => Memory: {memory}")

    print("\nTotal Page Faults:", page_faults)
    print("Total Page Hits  :", page_hits)

# ---- Main Execution ----
if __name__ == "__main__":
    ref_string = input("Enter page reference string (space-separated): ")
    frames = int(input("Enter number of frames: "))

    # Convert reference string to a list of integers
    pages = list(map(int, ref_string.strip().split()))

    fifo_page_replacement(pages, frames)
