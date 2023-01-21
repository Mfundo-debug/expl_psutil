""" 
Monitoring network: You can use the psutil.net_io_counters() function to get information about the system's network usage.
"""
import psutil
import time

while True:
    net_io_counters = psutil.net_io_counters()
    print(f"Bytes sent: {net_io_counters.bytes_sent}")
    print(f"Bytes received: {net_io_counters.bytes_recv}")
    time.sleep(1)