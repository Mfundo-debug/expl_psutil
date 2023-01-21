#process, using the function to iterate over all running processess and get information about each process
import psutil

for proc in psutil.process_iter():
    print(proc.name())