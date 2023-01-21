""" 
Monitoring disk: You can use the psutil.disk_io_counters() function to get information about the system's disk usage

"""
import psutil
import time
while True:
    disk_io_counters = psutil.disk_io_counters()
    print(f"Bytes read: {disk_io_counters.read_bytes}")
    print(f'Bytes written: {disk_io_counters.write_bytes}')
    time.sleep(1)