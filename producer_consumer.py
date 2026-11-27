import threading
import time
BUFFER_SIZE = 5
ITEMS = 10
buffer = []
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)
mutex = threading.Lock()
def producer():
    for item in range(1, ITEMS + 1):
        empty.acquire()
        with mutex:
            buffer.append(item)
            print(f"Producer produced item {item} at slot {(len(buffer) - 1)}")
        full.release()
        time.sleep(0.1)
def consumer():
    for _ in range(ITEMS):
        full.acquire()
        with mutex:
            item = buffer.pop(0)
            print(f"	Consumer consumed item {item}")
        empty.release()
        time.sleep(0.15)
def main():
    prod = threading.Thread(target=producer)
    cons = threading.Thread(target=consumer)
    prod.start(); cons.start()
    prod.join(); cons.join()
    print("All items produced and consumed.")
if __name__ == "__main__":
    main()
