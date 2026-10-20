
import psutil
from datetime import datetime

# Get the current date and time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Measure CPU, memory, and disk usage
cpu_usage = psutil.cpu_percent(interval=1)

memory = psutil.virtual_memory()
memory_usage = memory.percent

disk = psutil.disk_usage("/")
disk_usage = disk.percent

# Store the results in a list
results = [
    "===== SERVER HEALTH MONITOR =====",
    f"Check time: {current_time}",
    f"CPU Usage: {cpu_usage}%",
    f"Memory Usage: {memory_usage}%",
    f"Disk Usage: {disk_usage}%"
]

# Check CPU usage
if cpu_usage >= 80:
    results.append("WARNING: High CPU usage!")
else:
    results.append("CPU Status: NORMAL")

# Check memory usage
if memory_usage >= 80:
    results.append("WARNING: High memory usage!")
else:
    results.append("Memory Status: NORMAL")

# Check disk usage
if disk_usage >= 80:
    results.append("WARNING: Low disk space!")
else:
    results.append("Disk Status: NORMAL")

results.append("===== MONITORING COMPLETE =====")

# Display all results in the terminal
for line in results:
    print(line)

# Save results to a log file
with open("health_log.txt", "a") as log_file:
    for line in results:
        log_file.write(line + "\n")
    log_file.write("\n")

print("Results saved to health_log.txt")

