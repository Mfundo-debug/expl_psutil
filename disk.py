import psutil
import shutil
import os

# Get the list of all running processes
def get_running_processes():
    processes = []
    for proc in psutil.process_iter():
        processes.append(proc.name())
    return processes

# Function to check for unnecessary files and delete them
def clean_files(directory):
    for item in os.listdir(directory):
        s = os.path.join(directory, item)
        if os.path.isfile(s):
            response = input(f"Do you want to delete {item}? (yes/no)")
            if response.lower() == "yes":
                os.remove(s)
            else:
                print(f"{item} will not be deleted.")


# Function to check for unnecessary programs and uninstall them
def clean_programs():
    for item in os.listdir("C:/Program Files"):
        # Check if the program is not needed
        if item not in ["Program1", "Program2"]:
            response = input(f"Do you want to uninstall {item}? (yes/no)")
            if response.lower() == "yes":
                os.system(f"wmic product where name='{item}' call uninstall")
            else:
                print(f"{item} will not be uninstalled.")


# Check CPU usage
cpu_percent = psutil.cpu_percent()
if cpu_percent > 70:
    print("CPU usage is high, closing unnecessary processes...")
    for proc in get_running_processes():
        # Check if the process is not needed
        if proc not in ["process1", "process2"]:
            response = input(f"Do you want to taskkill {proc}? (yes/no)")
            if response.lower() == "yes":
                os.system(f"taskkill /im {proc}.exe /f")
            else:
                print(f"{proc} will not be stopped")

# Check Memory usage
memory = psutil.virtual_memory()
if memory.percent > 90:
    print("Memory usage is high, cleaning unnecessary files...")
    clean_files("C:/temp")

# Check Disk usage
disk = psutil.disk_usage('/')
if disk.percent > 80:
    print("Disk usage is high, cleaning unnecessary files and programs...")
    clean_files("C:/temp")
    clean_programs()

