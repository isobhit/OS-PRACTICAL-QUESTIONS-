MAX_BLOCKS = 30
def reset_disk():
    return [0] * MAX_BLOCKS  # 0 = free, 1 = allocated
def contiguous_allocation():
    disk = reset_disk()
    nf = int(input("Enter number of files: "))
    for f in range(nf):
        start, length = map(int, input(f"File {f + 1} - starting block, length: ").split())
        if start < 0 or length <= 0 or start + length > MAX_BLOCKS or any(disk[i] for i in range(start, start + length)):
            print("Allocation failed: blocks not free/out of range."); continue
        for i in range(start, start + length): disk[i] = 1
        print(f"File {f + 1} allocated blocks {start} to {start + length - 1}")
def linked_allocation():
    disk = reset_disk()
    nf = int(input("Enter number of files: "))
    for f in range(nf):
        length = int(input(f"File {f + 1} - number of blocks: "))
        free = [i for i, used in enumerate(disk) if not used][:length]
        for block in free: disk[block] = 1
        print(f"File {f + 1} allocated blocks: " + " -> ".join(map(str, free)) + " -> NULL")
        if len(free) < length: print("Warning: disk full, could not allocate all blocks.")
def indexed_allocation():
    disk = reset_disk()
    nf = int(input("Enter number of files: "))
    for f in range(nf):
        length = int(input(f"File {f + 1} - number of data blocks needed: "))
        free = [i for i, used in enumerate(disk) if not used]
        if len(free) < length + 1:
            print("Allocation failed: not enough free blocks."); continue
        index_block = free[0]
        data_blocks = free[1:length + 1]
        disk[index_block] = 1
        for block in data_blocks: disk[block] = 1
        print(f"File {f + 1} - Index block: {index_block}, Data blocks: {data_blocks}")
def main():
    print("Menu:\n1. Contiguous Allocation\n2. Linked Allocation\n3. Indexed Allocation")
    choice = int(input("Enter choice: "))
    if choice == 1: contiguous_allocation()
    elif choice == 2: linked_allocation()
    elif choice == 3: indexed_allocation()
    else: print("Invalid choice")
if __name__ == "__main__":
    main()
