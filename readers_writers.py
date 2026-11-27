import threading
import time
mutex = threading.Semaphore(1)
wrt = threading.Semaphore(1)
read_count = 0
shared_data = 0
def reader(reader_id):
    global read_count
    mutex.acquire()
    read_count += 1
    if read_count == 1:
        wrt.acquire()  # First reader locks the shared resource
    mutex.release()
    print(f"Reader {reader_id}: read shared_data = {shared_data}")
    time.sleep(0.2)
    mutex.acquire()
    read_count -= 1
    if read_count == 0:
        wrt.release()  # Last reader unlocks the resource
    mutex.release()
def writer(writer_id):
    global shared_data
    wrt.acquire()
    shared_data += 1
    print(f"Writer {writer_id}: wrote shared_data = {shared_data}")
    time.sleep(0.3)
    wrt.release()
def main():
    threads = [threading.Thread(target=writer, args=(1,))]
    threads += [threading.Thread(target=reader, args=(i,)) for i in range(1, 6)]
    threads += [threading.Thread(target=writer, args=(2,))]
    for t in threads: t.start()
    for t in threads: t.join()
if __name__ == "__main__":
    main()
