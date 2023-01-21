## cpu usage by core

import psutil
print(psutil.cpu_percent(percpu=True))