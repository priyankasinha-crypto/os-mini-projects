import psutil
import time

print("Personal Task Manager")
print("-" * 60)

for process in psutil.process_iter(
    ['pid', 'name', 'cpu_percent', 'memory_percent']
):
    try:
        info = process.info

        print(
            f"PID: {info['pid']} | "
            f"Name: {info['name']} | "
            f"CPU: {info['cpu_percent']}% | "
            f"Memory: {info['memory_percent']:.2f}%"
        )

    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass
