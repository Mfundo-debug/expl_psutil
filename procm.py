#processes by memory usage

import psutil

for proc in psutil.process_iter():
    print(proc.memory_info().rss)