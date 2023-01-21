#disk usage to get info about the system disk usage
import psutil 
disk = psutil.disk_usage('/')
print(disk.percent)