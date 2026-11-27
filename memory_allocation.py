def first_fit(blocks, processes):
    free = blocks[:]; result = [-1] * len(processes)
    for i, size in enumerate(processes):
        for j in range(len(free)):
            if free[j] >= size:
                result[i] = j; free[j] -= size; break
    return result
def best_fit(blocks, processes):
    free = blocks[:]; result = [-1] * len(processes)
    for i, size in enumerate(processes):
        choices = [j for j, space in enumerate(free) if space >= size]
        if choices:
            j = min(choices, key=lambda x: free[x])
            result[i] = j; free[j] -= size
    return result
def worst_fit(blocks, processes):
    free = blocks[:]; result = [-1] * len(processes)
    for i, size in enumerate(processes):
        choices = [j for j, space in enumerate(free) if space >= size]
        if choices:
            j = max(choices, key=lambda x: free[x])
            result[i] = j; free[j] -= size
    return result
def display(name, processes, allocation):
    print(f"\n--- {name} ---")
    print("Process No.\tProcess Size\tBlock No.")
    for i, size in enumerate(processes):
        block = f"B{allocation[i] + 1}" if allocation[i] != -1 else "Not Allocated"
        print(f"P{i + 1}\t\t{size}\t\t{block}")
def main():
    bn = int(input("Enter number of memory blocks: "))
    blocks = list(map(int, input("Enter sizes of blocks: ").split()))
    pn = int(input("Enter number of processes: "))
    processes = list(map(int, input("Enter sizes of processes: ").split()))
    if bn != len(blocks) or pn != len(processes) or any(x <= 0 for x in blocks + processes):
        print("Please enter valid positive sizes and matching counts."); return
    display("First Fit", processes, first_fit(blocks, processes))
    display("Best Fit", processes, best_fit(blocks, processes))
    display("Worst Fit", processes, worst_fit(blocks, processes))
if __name__ == "__main__":
    main()
