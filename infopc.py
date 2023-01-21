import psutil
#get cpu usage
cpu_percent = psutil.cpu_percent()
print("CPU usage: ", cpu_percent, "%")

#get memory usage
memory = psutil.virtual_memory()
print("Memory usage: ", memory.percent, "%")

#get disk usage
disk = psutil.disk_usage('/')
print("Disk usage: ", disk.percent, "%")

#get boot time
boot_time = psutil.boot_time()
print("Boot Time: ", boot_time)