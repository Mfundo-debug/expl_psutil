#Memory usage gives information about the system's memory usage
import psutil
mem = psutil.virtual_memory()
print(mem.percent)