import psutil
import time
from datetime import datetime, timedelta

def get_uptime():
    boot_time = psutil.boot_time()
    uptime = time.time() - boot_time
    return str(timedelta(seconds=int(uptime)))

while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    uptime = get_uptime()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    line = f"{timestamp} | CPU: {cpu}% | Memory: {memory}% | Disk: {disk}% | Uptime: {uptime}\n"

    print(line)

    # Save to file
    with open("health_log.txt", "a") as f:
        f.write(line)

    time.sleep(10)
