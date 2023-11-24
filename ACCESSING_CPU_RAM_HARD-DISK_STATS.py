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
#but if you just want to display let us say the system mode using cpu_times
print(psutil.cpu_times().system)
#cpu_states will give you the stats for ctx_switches, interrupts, soft_interrupts, syscalls
print(psutil.cpu_stats())
#cpu_freq will give you the current, minimum, maximum, frequency of the central-processing-unit
print(psutil.cpu_freq())

#RAM
#virtual_memory display total virtual memory, available memory, memory percentage, used memory, free memory, active memory, inactive memory, wired memory
print(psutil.virtual_memory())
#swap memory will display total swap memory, used swap memory, free swap memory, memory swap percentage, swap input memory, swap output memory
print(psutil.swap_memory())

#HARD-DISK
#disk_usage displays total disk usage, used disk, free disk available to use, percentage disk usage
print(psutil.disk_usage('/').percent)
#disk_partitions displays all the list partitions
print(psutil.disk_partitions())
