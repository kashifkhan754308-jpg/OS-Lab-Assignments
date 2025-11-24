# Indexed File Allocation Simulation

total_blocks = int(input("Enter total number of blocks: "))
block_status = [0] * total_blocks  # 0 = free, 1 = allocated

n = int(input("Enter number of files: "))

for i in range(n):
    index = int(input(f"\nEnter index block for file {i+1}: "))

    # Check if index block is free
    if block_status[index] == 1:
        print("Index block already allocated.")
        continue

    count = int(input("Enter number of data blocks: "))
    data_blocks = list(map(int, input("Enter block numbers: ").split()))

    # Validate input
    if len(data_blocks) != count:
        print("Invalid input: number of blocks does not match count.")
        continue

    if any(blk >= total_blocks or block_status[blk] == 1 for blk in data_blocks):
        print("Block(s) already allocated or invalid block number.")
        continue

    # Allocate index block and data blocks
    block_status[index] = 1
    for blk in data_blocks:
        block_status[blk] = 1

    print(f"File {i+1} allocated successfully.")
    print(f"Index Block: {index}")
    print(f"Data Blocks: {data_blocks}")

# Display final allocation table
print("\nFinal Block Status:")
for i in range(total_blocks):
    print(f"Block {i}: {'Allocated' if block_status[i] == 1 else 'Free'}")
