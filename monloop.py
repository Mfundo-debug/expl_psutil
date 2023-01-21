"""
Monitoring process: You can use the psutil.Process() function to get a handle to a specific process and then use the .cpu_percent() method to get the percentage of CPU usage for that process
"""

import psutil

p = psutil.Process(1234)
while True:
    print(p.cpu_percent())
    time.sleep(1)