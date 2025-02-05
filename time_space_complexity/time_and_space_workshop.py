#%%
import numpy as np 
from timeit import timeit
from timeit import repeat
import random 

#%% Test the speed of Numpy vs. Lists"
import numpy as np
   
n_elements = 10000

def sum_numpy():
    x = np.arange(n_elements)
    return x.sum()

def sum_list():
    y = range(n_elements)
    return sum(y)
    
t_numpy = timeit(sum_numpy, number = 10000)
t_list = timeit(sum_list, number = 10000)

print("numpy sums:", t_numpy)
print("list sums:", t_list)

print("numpy compared to lists:", f"{t_numpy/t_list:.2%}")

#%% Code can also be passed in as strings
#   In this case, necessary imports must be included in setup code

sum_numpy = """
x = np.arange(n_elements)
x.sum()"""

sum_list = """
y = range(n_elements)
sum(y)"""

setup_code = """
import numpy as np
n_elements = 10000
"""

t_numpy = timeit(sum_numpy, number = 10000, setup = setup_code)
t_list = timeit(sum_list, number = 10000, setup = setup_code)

print("numpy sums:", t_numpy)
print("list sums:", t_list)

print("numpy compared to lists:", f"{t_numpy/t_list:.2%}")

#%% Alternatively, give access to the globals namespace, which includes
#   imported modules.
import numpy as np
   
n_elements = 10000

sum_numpy = """
x = np.arange(n_elements)
x.sum()"""

sum_list = """
y = range(n_elements)
sum(y)"""

t_numpy = timeit(sum_numpy, number = 10000, globals=globals())
t_list = timeit(sum_list, number = 10000, globals=globals())

print("numpy sums:", t_numpy)
print("list sums:", t_list)

print("numpy compared to lists:", f"{t_numpy/t_list:.2%}")

#%% You will get more stable estimates using the repeat method of the timeit
#   module. This does *not* repeat setup code, if any

import numpy as np
   
n_elements = 10000

sum_numpy = """
x = np.arange(n_elements)
x.sum()"""

sum_list = """
y = range(n_elements)
sum(y)"""

setup_code = """
import numpy as np
n_elements = 10000
"""

t_numpy = repeat(sum_numpy, number = 1000, repeat = 5, globals=globals())
t_list = repeat(sum_list, number = 1000, repeat = 5, globals=globals())

print("numpy sums:", t_numpy)
print("list sums:", t_list)

# Use min for comparison
print("numpy compared to lists:", f"{min(t_numpy)/min(t_list):.2%}")


#%% Python program for implementation of Bubble Sort 

import random

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
  


test_code1='''
arr = [64, 34, 25, 12, 22, 11, 90, 74]
bubbleSort(arr)
'''

test_code2='''
rand_arr = random.sample(range(1000), 100)
bubbleSort(rand_arr)
'''

# Number defaults to 1,000,000
# print(timeit(stmt = test_code1, setup = setup_code1))
print(timeit(test_code1, globals=globals()))
# Sorting a list of 100 elements is slower. Reduce number to 1,000, repeat 5 times
#print(repeat(stmt = test_code2, setup = setup_code2, number = 1000, repeat= 5))  
print(repeat(test_code2, number = 1000, repeat=5, globals=globals()))   

#%%Bubble sort-- optimized form

import random

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
  
# Python3 Optimized implementation
# of Bubble sort
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


test_code1='''
rand_arr = random.sample(range(1000), 100)
bubbleSort(rand_arr)
'''

test_code2='''
rand_arr = random.sample(range(1000), 100)
bubbleSort_optim(rand_arr)
'''

t_bubble_sort = timeit(stmt=test_code1, number= 10000, globals=globals())
t_bubble_sort_optim = timeit(stmt=test_code2, number= 10000, globals=globals())

print("Basic bubblesort:", t_bubble_sort)
print("Optimized bubblesort:", t_bubble_sort_optim)

print("Basic bubblesort compared to optimized bubblesort:", f"{t_bubble_sort/t_bubble_sort_optim:.2%}")

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
quickSort(arr, low, high)
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

