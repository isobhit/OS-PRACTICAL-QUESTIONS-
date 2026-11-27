def calculate_times(processes, algorithm, quantum=None):
    # Each process: [pid, arrival, burst, priority]
    n = len(processes)
    remaining = [p[2] for p in processes]
    completion = [0] * n
    time = 0
    if algorithm == "FCFS":
        order = sorted(range(n), key=lambda i: (processes[i][1], i))
        for i in order:
            time = max(time, processes[i][1]) + processes[i][2]
            completion[i] = time
    elif algorithm in ("SJF", "Priority"):
        done = [False] * n
        count = 0
        while count < n:
            ready = [i for i, p in enumerate(processes)
                     if not done[i] and p[1] <= time]
            if not ready:
                time += 1
                continue
            if algorithm == "SJF":
                idx = min(ready, key=lambda i: (processes[i][2], processes[i][1], i))
            else:  # Lower priority number means higher priority
                idx = min(ready, key=lambda i: (processes[i][3], processes[i][1], i))
            time = max(time, processes[idx][1]) + processes[idx][2]
            completion[idx] = time
            done[idx] = True
            count += 1
    elif algorithm == "Round Robin":
        if quantum is None or quantum <= 0:
            raise ValueError("Time quantum must be positive.")
        from collections import deque
        order = sorted(range(n), key=lambda i: (processes[i][1], i))
        queue, next_idx = deque(), 0
        while next_idx < n or queue:
            if not queue and next_idx < n and time < processes[order[next_idx]][1]:
                time = processes[order[next_idx]][1]
            while next_idx < n and processes[order[next_idx]][1] <= time:
                queue.append(order[next_idx]); next_idx += 1
            if not queue:
                continue
            idx = queue.popleft()
            run = min(quantum, remaining[idx])
            time += run
            remaining[idx] -= run
            while next_idx < n and processes[order[next_idx]][1] <= time:
                queue.append(order[next_idx]); next_idx += 1
            if remaining[idx] > 0:
                queue.append(idx)
            else:
                completion[idx] = time
    else:
        raise ValueError("Invalid scheduling algorithm")
    rows = []
    for i, (pid, arrival, burst, priority) in enumerate(processes):
        tat = completion[i] - arrival
        wt = tat - burst
        rows.append((pid, arrival, burst, completion[i], tat, wt))
    print("\nPID\tAT\tBT\tCT\tTAT\tWT")
    for row in rows:
        print(*row, sep="	")
    print(f"Average Waiting Time = {sum(r[5] for r in rows) / n:.2f}")
    print(f"Average Turnaround Time = {sum(r[4] for r in rows) / n:.2f}")
def main():
    n = int(input("Enter number of processes: "))
    if n <= 0:
        print("Number of processes must be positive."); return
    processes = []
    for i in range(n):
        at, bt, pr = map(int, input(
            f"Process {i + 1} - Arrival Time, Burst Time, Priority: ").split())
        if at < 0 or bt <= 0:
            print("Arrival time must be non-negative and burst time positive."); return
        processes.append([i + 1, at, bt, pr])
    print("\n1. FCFS\n2. SJF (Non-preemptive)\n3. Priority (Non-preemptive)\n4. Round Robin")
    choice = int(input("Enter choice: "))
    names = {1: "FCFS", 2: "SJF", 3: "Priority", 4: "Round Robin"}
    if choice not in names:
        print("Invalid choice"); return
    quantum = int(input("Enter time quantum: ")) if choice == 4 else None
    calculate_times(processes, names[choice], quantum)
if __name__ == "__main__":
    main()
