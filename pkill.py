#kill a process
import psutil
p = psutil.Process(1234)
p.kill()