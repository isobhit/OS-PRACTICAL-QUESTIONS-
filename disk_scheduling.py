def distance(a, b):
    return abs(a - b)
def fcfs(requests, head):
    total, current = 0, head
    for track in requests:
        total += distance(current, track); current = track
    return total
def sstf(requests, head):
    pending = requests[:]; total = 0; current = head
    while pending:
        track = min(pending, key=lambda x: distance(current, x))
        total += distance(current, track); current = track; pending.remove(track)
    return total
def scan(requests, head, disk_size):
    left = sorted(x for x in requests if x < head)
    right = sorted(x for x in requests if x >= head)
    total, current = 0, head
    for track in right:
        total += distance(current, track); current = track
    if current != disk_size - 1:
        total += distance(current, disk_size - 1); current = disk_size - 1
    for track in reversed(left):
        total += distance(current, track); current = track
    return total
def cscan(requests, head, disk_size):
    left = sorted(x for x in requests if x < head)
    right = sorted(x for x in requests if x >= head)
    total, current = 0, head
    for track in right:
        total += distance(current, track); current = track
    if left:
        total += distance(current, disk_size - 1) + (disk_size - 1)
        current = 0
        for track in left:
            total += distance(current, track); current = track
    return total
def main():
    n = int(input("Enter number of requests: "))
    requests = list(map(int, input("Enter the requests: ").split()))
    head = int(input("Enter initial head position: "))
    disk_size = int(input("Enter disk size (max cylinder + 1): "))
    if n != len(requests) or disk_size <= 0 or not 0 <= head < disk_size or any(not 0 <= x < disk_size for x in requests):
        print("Invalid disk/request values."); return
    print("FCFS   total head movement =", fcfs(requests, head))
    print("SSTF   total head movement =", sstf(requests, head))
    print("SCAN   total head movement =", scan(requests, head, disk_size))
    print("C-SCAN total head movement =", cscan(requests, head, disk_size))
if __name__ == "__main__":
    main()
