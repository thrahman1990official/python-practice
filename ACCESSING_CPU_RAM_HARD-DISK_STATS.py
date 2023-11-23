#psutil (process and system utilities) is a cross-platform library for retrieving information on running processes and system 
#utilization (CPU, memory, disks, network, sensors) in Python. It is useful mainly for system monitoring, profiling and 
#limiting process resources and management of running processes.
import psutil

#CPU
#cpu_count will give you number of cores in the CPU
#logical=False will only give you the physical cores
print(psutil.cpu_count(logical=False))
#cpu_percent will give you current cpu usage as a percentage
#we need give an interval of 1 second for the cpu usage percentage
print(psutil.cpu_percent(interval=1))
#cpu_times will give you the seconds that cpu has spent as a user, nice, system, idle mode
print(psutil.cpu_times())
