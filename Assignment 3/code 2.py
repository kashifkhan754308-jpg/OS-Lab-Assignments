
# Sequential File Allocation Simulation

total_blocks = int(input("Enter total number of blocks: "))
block_status = [0] * total_blocks  # 0 = free, 1 = allocated

n = int(input("Enter number of files: "))

for i in range(n):
    start = int(input(f"\nEnter starting block for file {i+1}: "))
    length = int(input(f"Enter length of file {i+1}: "))
    allocated = True

    # Check if all required blocks are free and within bounds
    for j in range(start, start + length):
        if j >= total_blocks or block_status[j] == 1:
            allocated = False
            break

    # Allocate blocks if possible
    if allocated:
        for j in range(start, start + length):
            block_status[j] = 1
        print(f"File {i+1} allocated from block {start} to {start + length - 1}")
    else:
        print(f"File {i+1} cannot be allocated (insufficient space or block already occupied).")

# Display final block allocation status
print("\nFinal Block Status:")
for i in range(total_blocks):
    print(f"Block {i}: {'Allocated' if block_status[i] == 1 else 'Free'}")
