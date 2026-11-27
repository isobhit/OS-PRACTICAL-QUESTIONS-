import threading
NUM_THREADS = 4
def sum_array(start, end, results, index):
    total = sum(range(start, end))
    results[index] = total
    print(f"Thread {index + 1}: sum[{start}..{end}) = {total}")
def main():
    n = 1_000_000
    chunk = n // NUM_THREADS
    results = [0] * NUM_THREADS
    threads = []
    for i in range(NUM_THREADS):
        start = i * chunk
        end = n if i == NUM_THREADS - 1 else (i + 1) * chunk
        t = threading.Thread(target=sum_array,
                             args=(start, end, results, i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Total sum (0 to {n - 1}) computed using {NUM_THREADS} threads = {sum(results)}")
if __name__ == "__main__":
    main()
