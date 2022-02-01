import random
import time
from time import process_time_ns
from time import perf_counter_ns
import cProfile
import pstats

#%% script for profiling with the command prompt

def expensive_function():
    execution_time = random.random() / 100
    time.sleep(execution_time)
    
if __name__ == '__main__':
    for _ in range(1000):
        expensive_function()
        
#%% CPU profiling
#Download the cpu_profiling.py file, and in your command line run:
    
```
python -m cProfile --sort cumtime cpu_profiling.py
```
    
    *** make sure to navigate to the correct directory first ***
#%% time.process_time (), process_time_ns()
#is a value which is derived from the CPU counter but updated only 
#when a given process is running on the CPU and can be broken down 
#into 'user time', which is the time when the process itself is 
#running on the CPU, and 'system time', which is the time when the 
#operating system kernel is running on the CPU on behalf on the process.

from time import process_time_ns

#start counter
t1_start= process_time_ns()
for i in range(50, 100, 2):
    print(i)
    
#stop the counter
t1_stop= process_time_ns()

#%% time.perf_counter_ns()

from time import perf_counter_ns

#start counter
t1_start= perf_counter_ns()
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
  
# Driver code to test above
arr = [8, 7, 2, 1, 0, 9, 6]

bubbleSort(arr)
    
#stop the counter
t1_stop= perf_counter_ns()
print(t1_stop-t1_start)

#%% cProfile module
import cProfile

with cProfile.Profile() as pr:
    for i in range(50, 100, 2):
        print(i**3)

pr.print_stats()

#%% more complex program

import cProfile
import pstats
import random
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
  
# Driver code to test above
arr = [8, 7, 2, 1, 0, 9, 6]
#rand_arr= random.sample(range(1000), 100)

# Initialize profile class and call bubbleSort() function
profiler = cProfile.Profile()
profiler.enable()
bubbleSort(arr)
profiler.disable()
stats = pstats.Stats(profiler).sort_stats('tottime')
#can sort by other attributes ('ncalls'), ('cumtime')

# Print the stats report
#stats.strip_dirs #function will make the result less cluttered
stats.print_stats()   


#%% Next goal, visualize with PyCallGraph = is a Python module that creates call graphs for 
#Python programs. It generates a PNG file showing an modules's 
#function calls and their link to other function calls, the amount 
#of times a function was called and the time spent in that function.


