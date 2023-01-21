#process by name:
import psutil
for proc in psutil.process_iter(attrs=['pid','name']):
        print(proc.info)