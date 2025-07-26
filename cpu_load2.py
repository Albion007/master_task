import time
import multiprocessing
import argparse
import requests
import psutil
import csv
import subprocess


def load_test(url, stop_time, counter, error_counter, response_times):
    while time.time() < stop_time:
        start = time.time()
        try:
            response = requests.get(url, timeout=10)
            response_times.append(time.time() - start)
            counter.value += 1
        except Exception:
            error_counter.value += 1


def measure_with_curl(url):
    """
    Uses curl to measure DNS lookup, connect, TTFB, and total times.
    Returns a dict with float values in seconds.
    """
    cmd = [
        'curl', '-o', '/dev/null', '-s',
        '-w',
        'namelookup:%{time_namelookup},connect:%{time_connect},starttransfer:%{time_starttransfer},total:%{time_total}',
        url
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    out = proc.stdout.strip()
    parts = dict(pair.split(':') for pair in out.split(','))
    return {k: float(v) for k, v in parts.items()}


def run_test(url, num_processes, filename, duration):
    stop_time = time.time() + duration
    manager = multiprocessing.Manager()
    counter = manager.Value('i', 0)
    error_counter = manager.Value('i', 0)
    response_times = manager.list()

    # Fillimi i matjes së sistemit
    cpu_start = psutil.cpu_percent(interval=None)
    mem_start = psutil.virtual_memory().used
    net_start = psutil.net_io_counters()

    processes = []
    for _ in range(num_processes):
        p = multiprocessing.Process(
            target=load_test,
            args=(url, stop_time, counter, error_counter, response_times)
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    # Fundi i matjes së sistemit
    cpu_end = psutil.cpu_percent(interval=None)
    mem_end = psutil.virtual_memory().used
    net_end = psutil.net_io_counters()

    avg_response_time = sum(response_times) / len(response_times) if response_times else 0

    # Matjet me curl
    curl_metrics = measure_with_curl(url)

    # Ruaj rezultatet
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Metric', 'Value'])
        writer.writerow(['Test Duration (s)', duration])
        writer.writerow(['Processes Used', num_processes])
        writer.writerow(['URL', url])
        writer.writerow(['Total Requests', counter.value])
        writer.writerow(['Failed Requests', error_counter.value])
        writer.writerow(['Average Response Time (s)', round(avg_response_time, 4)])
        writer.writerow(['CPU Usage (%)', cpu_end])
        writer.writerow(['RAM Usage Change (MB)', round((mem_end - mem_start) / 1024 / 1024, 2)])
        writer.writerow(['Network Sent (MB)', round((net_end.bytes_sent - net_start.bytes_sent) / 1024 / 1024, 2)])
        writer.writerow(['Network Received (MB)', round((net_end.bytes_recv - net_start.bytes_recv) / 1024 / 1024, 2)])
        # Shtojmë kolonat e curl-it
        writer.writerow(['Curl DNS Lookup (s)', curl_metrics['namelookup']])
        writer.writerow(['Curl Connect Time (s)', curl_metrics['connect']])
        writer.writerow(['Curl TTFB (s)', curl_metrics['starttransfer']])
        writer.writerow(['Curl Total Time (s)', curl_metrics['total']])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True)
    parser.add_argument('--processes', type=int, default=4)
    parser.add_argument('--file', default='results.csv')
    parser.add_argument('--duration', type=int, default=30)
    args = parser.parse_args()

    run_test(args.url, args.processes, args.file, args.duration)
