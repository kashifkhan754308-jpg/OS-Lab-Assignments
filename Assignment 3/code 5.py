
# Memory Management Simulation
# Strategies: MFT (Fixed Partitioning) and MVT (Variable Partitioning)

def MFT():
    print("\n--- MFT (Fixed Partitioning) Simulation ---")
    mem_size = int(input("Enter total memory size: "))
    part_size = int(input("Enter partition size: "))
    n = int(input("Enter number of processes: "))

    partitions = mem_size // part_size
    print(f"\nTotal partitions created: {partitions}\n")

    for i in range(n):
        psize = int(input(f"Enter size of Process {i+1}: "))
        if psize <= part_size:
            print(f"Process {i+1} of size {psize} KB allocated.")
        else:
            print(f"Process {i+1} of size {psize} KB too large for a fixed partition.")

    print("\nNote: Some partitions may remain unused (internal fragmentation possible).")


def MVT():
    print("\n--- MVT (Variable Partitioning) Simulation ---")
    mem_size = int(input("Enter total memory size: "))
    n = int(input("Enter number of processes: "))

    for i in range(n):
        psize = int(input(f"Enter size of Process {i+1}: "))
        if psize <= mem_size:
            print(f"Process {i+1} of size {psize} KB allocated.")
            mem_size -= psize
            print(f"Remaining memory: {mem_size} KB")
        else:
            print(f"Process {i+1} cannot be allocated. Not enough memory ({mem_size} KB left).")

    print("\nNote: Memory is allocated dynamically (external fragmentation possible).")


# --- Main Program ---
print("MFT Simulation:")
MFT()

print("\nMVT Simulation:")
MVT()
