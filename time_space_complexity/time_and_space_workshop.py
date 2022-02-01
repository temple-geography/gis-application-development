
import numpy as np #for numpy operations
from numpy import arange #to create lists
import timeit # to test the performance of different solutions
from timeit import Timer 
from sys import getsizeof #to check the size of memory different objects take
from timeit import repeat #for repeated timing runs
import random #for creating random lists

#%% SIZE: We can use the getsizeof function to measure how much space a list or array uses
   
n_elements = 100000
x_list = [x for x in range(n_elements)]
getsizeof(x_list)
  
x_np = np.array(x_list)
getsizeof(x_np)
   
getsizeof(x_list) - getsizeof(x_np)
   
#%%Timing: Simple Timeit use case
   
print(timeit.timeit('output = 10 * 12'))
   
# Timing multiple lines of code: Use semicolons or triple quotes
   
print("The time taken is ",timeit.timeit(stmt='a=10;b=12;output=a*b'))
   
print(timeit.timeit('''
a = 10
b = 12
output = a*b
'''))
   
# You can define the number of times for timeit to run your code (the default is 1,000,000)
   
print(timeit.timeit('''
a = 10
b = 12
output = a*b
''', number = 200000))
   
# Functions can be passed from main into timeit"
   
def list1():
    L = [1,3,2,4,5,7,6,8]
    L.sort()
    
if __name__ == '__main__':
    print(timeit.timeit("list1()", setup = "from __main__ import list1"))

#%% Test the speed of Numpy vs. Lists"
from numpy import arange
   
Nelements = 10000
Ntimeits = 10000
    
x = arange(Nelements)
y = range(Nelements)
    
t_numpy = Timer("x.sum()","from __main__ import x")
t_list = Timer("sum(y)", "from __main__ import y")
   
print("numpy: %.3e" % (t_numpy.timeit(Ntimeits)/Ntimeits,))
print("list:  %.3e" % (t_list.timeit(Ntimeits)/Ntimeits,))
  
### Timeit can also be executed via the command line using: python -m timeit \"Statement....\""
### Timeit works best on small snippets of code, for larger code you can use CPU profiling at the command line"

#%% Test the speed of Numpy vs. Lists"
   
Nelements = 10000
Ntimeits = 10000
    
x = arange(Nelements)
y = range(Nelements)
    
t_numpy = Timer(\"x.sum()\", \"from __main__ import x\")
t_list = Timer(\"sum(y)\", \"from __main__ import y\")
   
print(\"numpy: %.3e\" % (t_numpy.timeit(Ntimeits)/Ntimeits,))
print(\"list:  %.3e\" % (t_list.timeit(Ntimeits)/Ntimeits,))
  
### Timeit can also be executed via the command line using: python -m timeit \"Statement....\""
### Timeit works best on small snippets of code, for larger code you can use CPU profiling at the command line"

#%% timeit.repeat function
# calls timeit() repeatedly and returns a list of results
#syntax: repeat(repeat=5, number=1000000)

print(timeit.repeat(stmt, setup, repeat))
#%% Python program for implementation of Bubble Sort 
  
def bubbleSort(arr):
    n = len(arr)
  
    # Traverse through all array elements
    for i in range(n):
  
        # Last i elements are already in place
        for j in range(0, n-i-1):
  
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
  


#create setup and test codes for timing
setup_code1='''
from __main__ import bubbleSort
'''
test_code1='''
arr = [64, 34, 25, 12, 22, 11, 90, 74]
'''
setup_code2='''
from __main__ import bubbleSort
import random
'''
test_code2='''
rand_arr= random.sample(range(1000), 100)
'''

print(timeit.timeit(stmt= test_code1, setup= setup_code, number=50))
print(timeit.repeat(stmt= test_code2, setup= setup_code, number= 1000000, repeat= 5))  
    
#%%Bubble sort-- optimized form

# Python3 Optimized implementation
# of Bubble sort

# An optimized version of Bubble Sort
def bubbleSort_optim(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n):
		swapped = False

		# Last i elements are already
		# in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to
			# n-i-1. Swap if the element
			# found is greater than the
			# next element
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True

		# IF no two elements were swapped
		# by inner loop, then break
		if swapped == False:
			break

#construct setup and test codes for timing		
setup_code1='''
from __main__ import bubbleSort_optim
'''
test_code1='''
arr = [64, 34, 25, 12, 22, 11, 90, 73]
'''
setup_code2='''
from __main__ import bubbleSort_optim
import random
'''
test_code2='''
random_arr= random.sample(range(1000), 100)
'''
print(timeit.timeit(stmt=test_code1, setup= setup_code1, number= 10000))
print(timeit.repeat(stmt=test_code2, setup=setup_code2, number= 1000000, repeat= 5))

#%%bubble sort w/out loop
 
# Function to implement bubble
# sort without using loops
def loopless_bubble_sort(arr):
   
    # Base Case: If array
    # contains a single element
    if len(arr) <= 1:
        return arr
       
    # Base Case: If array
    # contains two elements
    if len(arr) == 2:
        return arr if arr[0] < arr[1] else [arr[1], arr[0]]
 
    # Store the first two elements
    # of the list in variables a and b
    a, b = arr[0], arr[1]
 
    # Store remaining elements
    # in the list bs
    bs = arr[2:]
 
    # Store the list after
    # each recursive call
    res = []
     
    # If a < b
    if a < b:
        res = [a] + bubble_sort([b] + bs)
         
    # Otherwise, if b >= a
    else:
        res = [b] + bubble_sort([a] + bs)
         
    # Recursively call for the list
    # less than the last element and
    # and return the newly formed list
    return bubble_sort(res[:-1]) + res[-1:]
 
 
#Task: Construct the test and setup codes for the following variables
arr = [1, 3, 4, 5, 6, 2, 11, 8, 34, 7, 9]

rand_arr= random.sample(range(1000), 100)


print(timeit.timeit(stmt= test_code1, setup= setup_code1, number= 1000))
print(timeit.repeat(stmt= test_code2, setup= setup_code2, number= 10000, repeat=5))

#%% selection sort= achieves the same result in a different way
import random

def selection_sort(arr, n):
     
    for i in range(n - 1):
        min_index = i 
         
        for j in range(i + 1, n):
            if (arr[j] < arr[min_index]):
                min_index = j
                 
        arr[i], arr[min_index] = arr[min_index], arr[i] 
         

setup_code1= '''
from  __main__ import selection_sort
'''
test_code1= '''
arr= [ 2, 0, 1, 4, 3 ]
n= len(arr)
'''
setup_code2= '''
from  __main__ import selection_sort
import random
'''
test_code2='''
rand_arr= random.sample(range(1000), 100)
n=len(rand_arr)
'''
#Task: Construct your timeit and timeit.repeat statements with the above code input
    
#%% QUICKSORT ~ partition-exchange sort = in-place sorting algorithm
#partitions the array around a pivot element>> sub-arrays, 
#partition sorted recursively<<requires less memory
#takes O(nlogn) comparisons for n items

#Syntax
# function to find the partition position
def partition(array, low, high):
    
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1

# function to perform quicksort
def quickSort(array, low, high):
    if low < high:

        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # recursive call on the right of pivot
        quickSort(array, pi + 1, high)


arr = [8, 7, 2, 1, 0, 9, 6]
rand_arr= random.sample(range(1000), 100)
n= len(arr)
#quickSort(arr, 0, n - 1)

#construct setup and test codes for timing
setup_code1='''
from  __main__ import quickSort
'''
test_code1='''
arr = [8, 7, 2, 1, 0, 9, 6]
n=len(arr)
low= 0
high= n-1
'''
setup_code2='''
from __main__ import quickSort
import random
'''
test_code2='''
rand_arr= random.sample(range(1000), 100)
n=len(arr)
low=0
high= n-1
'''
print(timeit.timeit(stmt= test_code2, setup= setup_code2, number= 10000))
print(timeit.repeat(stmt= test_code1, setup= setup_code1, number=100000, repeat=5))

