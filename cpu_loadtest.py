#kerkesa,
#Ruajtje automatike e rezultateve në një file .csv.
#Version me asyncio në vend të multiprocessing.
#Apo mënyrën si mund të bësh testime të ngjashme në cloud.

import argparse
import csv
import subprocess
import time
import psutil
from multiprocessing import Pool

def curl_request(url):
    start = time.time()
    # Ekzekutoni curl dhe merrni kohën e përgjigjes
    result = subprocess.run(
        ["curl", "-o", "/dev/null", "-s", "-w", "%{time_total}", url],
        capture_output=True,
        text=True
    )
    response_time = float(result.stdout.strip())
    cpu = psutil.cpu_percent(interval=None)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    return (timestamp, cpu, response_time)

def worker(args):
    url, filename = args
    data = curl_request(url)
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)
    return data

def main():
    parser = argparse.ArgumentParser(description="Load test with curl and CPU usage logging")
    parser.add_argument("--url", required=True, help="URL to test")
    parser.add_argument("--processes", type=int, default=4, help="Number of parallel processes")
    parser.add_argument("--file", default="results.csv", help="CSV file to save results")
    args = parser.parse_args()

    # Shto header në csv (vetëm në fillim)
    with open(args.file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "cpu_percent", "response_time_sec"])

    pool = Pool(args.processes)

    print(f"Starting load test on {args.url} with {args.processes} processes. Saving to {args.file}")
    try:
        while True:
            pool.map(worker, [(args.url, args.file)] * args.processes)
            time.sleep(1)  # Pushim 1 sekondë mes batch-eve
    except KeyboardInterrupt:
        print("Test stopped by user.")

if __name__ == "__main__":
    main()
