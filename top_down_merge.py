#Based on logic from Sedgewick and Wayne - Algorithms, 4th Edition

from copy import copy, deepcopy
import random

unsorted = []
for i in range(1,20):
    unsorted.append(int(round(random.random()*100)))#add random ints to unsorted

print("Unsorted list: ")
print(unsorted)

sorted = deepcopy(unsorted)

#initialize empty list to hold values
aux = [0]*len(sorted) 

def sort(a, lo, hi):
    if hi <= lo:
        return
    mid = lo + (hi-lo)/2
    sort(a, lo, mid) #sort 1st half
    sort(a, mid+1, hi) #sort second half
    merge(a, lo, mid,hi)

def merge(a, lo, mid, hi):
    i = lo
    j = mid + 1

    for k in range(lo,hi+1):
        aux[k] = a[k]

    for k in range(lo, hi+1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif aux[j] <= aux[i]:
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1

sort(sorted, 0, len(sorted)-1)

print("Sorted List: ")
print(sorted)
