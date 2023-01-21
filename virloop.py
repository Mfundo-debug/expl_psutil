""" 
Monitoring memory: You can use the psutil.virtual_memory() function to get the system's memory usage and the psutil.swap_memory() function to get the system's swap memory usage.
"""
import psutil
import time
while True:
    virtual_memory = psutil.virtual_memory()
    swap_memory = psutil.swap_memory()
    print(f"Virtual memory: {virtual_memory.percent}%")
    print(f"swap memory: {swap_memory.percent}%")
    time.sleep(1)
    