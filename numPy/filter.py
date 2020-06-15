"""
Filtering Array
Getting some elements out of an existing array and creating a new array
    out of them is called filtering.
In NumPy, you filter an array using a boolean index list.
If the value at an index is True that element is contained in the filtered
    array, if the value at that index is False that element is excluded from
    the filtered array.
"""
import numpy as np

# Create an array from the elements on index 1 and 2:

arr = np.array([10, 20, 30, 40])
something = [False, True, True, False]

ftarr = arr[something]

print(ftarr)

# Create a filter array that will return only values higher than 50:
arr = np.array([20, 40, 60, 80, 100])

ftr_arr = []

for some in arr:
    if some > 50:
        ftr_arr.append(True)
    else:
        ftr_arr.append(False)

newarr = arr[ftr_arr]

print(' ')
print(ftr_arr)
print(newarr)


# Create a filter array that will return only even elements from the
# original array:

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

even = []

for shae in arr:
    if shae % 2 == 0:
        even.append(True)
    else:
        even.append(False)

even_arr = arr[even]

print(' ')
print(even_arr)


"""
Creating Filter Directly From Array
"""

# Create a filter array that will return only values higher than 50:

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

ftr = arr > 50

ftr_arr = arr[ftr]

print(' ')
print(ftr)
print(ftr_arr)


"""
Create a filter array that will return only odd elements from the
    original array:
"""

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

ftr = arr % 2 != 0

ftr_arr = arr[ftr]

print(' ')
print(ftr)
print(ftr_arr)
