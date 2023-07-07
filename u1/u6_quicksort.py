from random import *
import time 
import sys

counter = 0

def my_partition(array):
    global counter                            # counts vergleiche
    i = -1
    n = len(array)-1

    k = randint(0,n)                          # random pivot
    pivot = array[k]                          # random pivot
    array[k], array[n] = array[n], array[k]   # random pivot

    for j in range(0, n):
        counter +=1                           # counts vergleiche
        if array[j] <= pivot:
            i = i+1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[n] = array[n], array[i+1]
    return (i+1)

def my_quicksort(array,b):
    if len(array) <= b:                                             #shranke b
        return monkeySort(array)
    pivot = my_partition(array)
    #left = [array[i] for i in range(0,pivot-1)]
    left = array[:pivot]
    right = array[pivot+1:]
    #right = [array[i] for i in range(pivot+1,len(array))]
    return my_quicksort(left, b) + [array[pivot]] + my_quicksort(right, b) 

def monkeySort(arr):
    while(is_sorted(arr)==False):
        shuffle(arr)
    return arr

def is_sorted(arr):
    global counter                  #counts vergleiche
    for i in range(0, len(arr)-1):
        counter +=1                 #counts vergleiche
        if (arr[i]>arr[i+1]):
            return False
    return True



def create_random_floatlist (n):
    array = []
    for i in range(0,n):
        array += [random()]
    return array
 
#main
length = 10000
array = create_random_floatlist(length)

print('Random array length = ', length)
for b in [1,3,5,8,10]:
    counter = 0
    begin = time.time()                 #measures time
    for i in range (0,10):
        array = create_random_floatlist(length)
        #print(is_sorted(array))
        array = my_quicksort(array,b)
        #print(is_sorted(array))
    end = time.time()                   #measures time
    print('b = ' ,b , ', Average_Counter: ' , counter/length , ', Exec_Time: ' , end-begin)
