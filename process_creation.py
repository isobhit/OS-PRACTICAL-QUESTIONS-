import os
import sys
print("Parent process: PID =", os.getpid())
try:
    pid = os.fork()  # Available on Linux/Unix
except AttributeError:
    print("os.fork() is not available on this operating system.")
    sys.exit(1)
if pid == 0:
    # Child process
    print(f"Child process: PID = {os.getpid()}, Parent PID = {os.getppid()}")
    print("Child is about to execute 'ls -l'")
    os.execvp("ls", ["ls", "-l"])  # Replaces the child process
else:
    # Parent process waits for the child
    print(f"Parent waiting for child (PID = {pid}) to finish...")
    child_pid, status = os.waitpid(pid, 0)
    if os.WIFEXITED(status):
        print("Child exited with status", os.WEXITSTATUS(status))
    print("Parent process resumes and exits.")
