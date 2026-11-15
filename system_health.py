import psutil
import time
import csv
import platform
from datetime import datetime, timedelta

# How often to collect data (in seconds)
INTERVAL = 5
CSV_FILE = "system_health.csv"

def get_uptime():
    # System boot time
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    return str(timedelta(seconds=int(uptime_seconds)))

def get_system_health():
    cpu = psutil.cpu_percent(interval=1)  # CPU usage in %
    
    memory = psutil.virtual_memory()
    mem_percent = memory.percent
    mem_used_gb = round(memory.used / (1024**3), 2)
    mem_total_gb = round(memory.total / (1024**3), 2)
    
    disk = psutil.disk_usage('/')  # Disk usage
    disk_percent = disk.percent
    disk_used_gb = round(disk.used / (1024**3), 2)
    disk_total_gb = round(disk.total / (1024**3), 2)
    
    uptime = get_uptime()
    
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_percent": cpu,
        "memory_percent": mem_percent,
        "memory_used_gb": mem_used_gb,
        "memory_total_gb": mem_total_gb,
        "disk_percent": disk_percent,
        "disk_used_gb": disk_used_gb,
        "disk_total_gb": disk_total_gb,
        "uptime": uptime,
        "os": f"{platform.system()} {platform.release()}"
    }

def main():
    print("System Health Monitor Started...")
    print(f"Collecting data every {INTERVAL} seconds. Press CTRL+C to stop.\n")

    # Create CSV file with header
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            "timestamp", "cpu_percent", "memory_percent",
            "memory_used_gb", "memory_total_gb",
            "disk_percent", "disk_used_gb", "disk_total_gb",
            "uptime", "os"
        ])
        writer.writeheader()

        try:
            while True:
                data = get_system_health()

                # Print on screen
                print(f"[{data['timestamp']}] CPU: {data['cpu_percent']}% | "
                      f"Memory: {data['memory_percent']}% ({data['memory_used_gb']}/{data['memory_total_gb']} GB) | "
                      f"Disk: {data['disk_percent']}% ({data['disk_used_gb']}/{data['disk_total_gb']} GB) | "
                      f"Uptime: {data['uptime']}")

                # Save to CSV
                writer.writerow(data)
                f.flush()

                time.sleep(INTERVAL)

        except KeyboardInterrupt:
            print("\nStopped. Data saved in system_health.csv")

if __name__ == "__main__":
    main()
