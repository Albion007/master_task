import sys
import subprocess
from multiprocessing import Process

def stress_with_curl(url: str):
    while True:
        subprocess.run(["curl", "-s", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Përdorimi: python3 cpu_load.py <URL> [numri_i_proceseve]")
        sys.exit(1)

    url = sys.argv[1]
    num_processes = int(sys.argv[2]) if len(sys.argv) > 2 else 4  # default 4 procese

    processes = []
    for _ in range(num_processes):
        p = Process(target=stress_with_curl, args=(url,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
