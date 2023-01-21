# cpu usage over time: use the function in a loop to ge the percentage of CPU usage over a period of time.
#this can be useful for monitoring the cpu usage and detecting performance issues
import psutil
import time

while True:
    print(psutil.cpu_percent())
    time.sleep(1)