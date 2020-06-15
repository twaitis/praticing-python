"""
You can search an array for a certain value, and return the indexes that
    get a match.
To search an array, use the where() method.

"""
import numpy as np

# find the indexes where the value is 3:

arr = np.array([1, 3, 5, 3, 9])

s = np.where(arr == 3)

print(s)

# Find the indexes where the values are odd:

arr = np.array([1, 2, 3, 4])
s = np.where(arr%2 != 0)
print(s)

# Find the indexes where the values are odd:

s = np.where(arr % 2 == 0)
print(s)

print(' ')
print(' ')
print(' ')
print(' ')

"""
Search Sorted
There is a method called searchsorted() which performs a binary search in
    the array, and returns the index where the specified value would be
    inserted to maintain the search order.

"""

# Find the indexes where the value 3 should be inserted:

arr = np.array([1, 2, 4, 5])
s = np.searchsorted(arr, 3)
print(s)



























