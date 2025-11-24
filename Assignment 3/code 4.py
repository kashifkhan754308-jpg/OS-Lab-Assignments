# Contiguous Memory Allocation Simulation
# Strategies: First Fit, Best Fit, Worst Fit

def allocate_memory(strategy, partitions, processes):
    print(f"\n--- {strategy.capitalize()} Fit Allocation ---")
    # Make a copy of partitions to avoid modifying the original
    parts = partitions.copy()
    allocation = [-1] * len(processes)

    for i, psize in enumerate(processes):
        idx = -1

        if strategy == "first":
            # First Fit: allocate the first partition that fits
            for j, part in enumerate(parts):
                if part >= psize:
                    idx = j
                    break

        elif strategy == "best":
            # Best Fit: allocate the smallest partition that fits
            best_fit = float("inf")
            for j, part in enumerate(parts):
                if part >= psize and part < best_fit:
                    best_fit = part
                    idx = j

        elif strategy == "worst":
            # Worst Fit: allocate the largest partition that fits
            worst_fit = -1
            for j, part in enumerate(parts):
                if part >= psize and part > worst_fit:
                    worst_fit = part
                    idx = j

        # Allocate process if possible
        if idx != -1:
            allocation[i] = idx
            parts[idx] -= psize

    # Display results
    for i, a in enumerate(allocation):
        if a != -1:
            print(f"Process {i+1} allocated in Partition {a+1}")
        else:
            print(f"Process {i+1} cannot be allocated")

# --- Main Program ---

# Take input only once
partitions = list(map(int, input("Enter partition sizes: ").split()))
processes = list(map(int, input("Enter process sizes: ").split()))

# Apply all three strategies using same input data
allocate_memory("first", partitions, processes)
allocate_memory("best", partitions, processes)
allocate_memory("worst", partitions, processes)
