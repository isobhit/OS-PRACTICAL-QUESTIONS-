def calculate_need(maximum, allocation):
    return [[maximum[i][j] - allocation[i][j]
             for j in range(len(maximum[0]))] for i in range(len(maximum))]
def safety_algorithm(available, maximum, allocation):
    n, r = len(allocation), len(available)
    need = calculate_need(maximum, allocation)
    work = available[:]
    finish = [False] * n
    safe_sequence = []
    while len(safe_sequence) < n:
        found = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(r)):
                work = [work[j] + allocation[i][j] for j in range(r)]
                finish[i] = True
                safe_sequence.append(i)
                found = True
        if not found:
            return False, []
    return True, safe_sequence
def main():
    n = int(input("Enter number of processes: "))
    r = int(input("Enter number of resource types: "))
    available = list(map(int, input("Enter available resources: ").split()))
    print("Enter maximum demand matrix row by row:")
    maximum = [list(map(int, input(f"P{i}: ").split())) for i in range(n)]
    print("Enter allocation matrix row by row:")
    allocation = [list(map(int, input(f"P{i}: ").split())) for i in range(n)]
    if len(available) != r or any(len(row) != r for row in maximum + allocation):
        print("Invalid matrix dimensions."); return
    if any(maximum[i][j] < allocation[i][j] for i in range(n) for j in range(r)):
        print("Allocation cannot exceed maximum demand."); return
    safe, sequence = safety_algorithm(available, maximum, allocation)
    if safe:
        print("System is in a SAFE state.")
        print("Safe sequence:", " -> ".join(f"P{i}" for i in sequence))
    else:
        print("System is NOT in a safe state.")
if __name__ == "__main__":
    main()
