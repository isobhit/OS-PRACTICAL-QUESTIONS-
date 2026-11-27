import threading
import time
N = 5
forks = [threading.Semaphore(1) for _ in range(N)]
room = threading.Semaphore(N - 1)  # At most N-1 philosophers compete for forks
def philosopher(philosopher_id):
    left = philosopher_id
    right = (philosopher_id + 1) % N
    for _ in range(2):
        print(f"Philosopher {philosopher_id} is thinking")
        time.sleep(0.1)
        room.acquire()
        forks[left].acquire()
        forks[right].acquire()
        print(f"Philosopher {philosopher_id} is eating (fork {left} and fork {right})")
        time.sleep(0.15)
        forks[right].release()
        forks[left].release()
        room.release()
        print(f"Philosopher {philosopher_id} finished eating and put down forks")
def main():
    threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]
    for t in threads: t.start()
    for t in threads: t.join()
if __name__ == "__main__":
    main()
