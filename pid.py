## process using process ID
import psutil
p = psutil.Process(1234)
print(p.name())
print(p.memory_info())