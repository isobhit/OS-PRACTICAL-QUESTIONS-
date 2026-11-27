def fifo(reference, frame_count):
    frames, pointer, faults = [], 0, 0
    for page in reference:
        if page not in frames:
            faults += 1
            if len(frames) < frame_count:
                frames.append(page)
            else:
                frames[pointer] = page
                pointer = (pointer + 1) % frame_count
    return faults
def lru(reference, frame_count):
    frames, last_used, faults = [], {}, 0
    for time, page in enumerate(reference):
        if page not in frames:
            faults += 1
            if len(frames) < frame_count:
                frames.append(page)
            else:
                victim = min(frames, key=lambda x: last_used[x])
                frames[frames.index(victim)] = page
        last_used[page] = time
    return faults
def optimal(reference, frame_count):
    frames, faults = [], 0
    for i, page in enumerate(reference):
        if page in frames:
            continue
        faults += 1
        if len(frames) < frame_count:
            frames.append(page)
        else:
            future = reference[i + 1:]
            next_use = {p: (future.index(p) if p in future else float('inf')) for p in frames}
            victim = max(frames, key=lambda p: next_use[p])
            frames[frames.index(victim)] = page
    return faults
def main():
    n = int(input("Enter number of pages in reference string: "))
    reference = list(map(int, input("Enter the reference string: ").split()))
    frame_count = int(input("Enter number of frames: "))
    if n != len(reference) or frame_count <= 0:
        print("Invalid input."); return
    print("FIFO Page Faults  =", fifo(reference, frame_count))
    print("LRU Page Faults   =", lru(reference, frame_count))
    print("Optimal Page Faults =", optimal(reference, frame_count))
if __name__ == "__main__":
    main()
