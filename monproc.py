#monitoring process
# to get handle to specific process
import psutil
p = psutil.Process(1234)
info = p.as_dict(attrs=['pid','name','cpu_percent', 'memory_info','create_time'])
print(info)