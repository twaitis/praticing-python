"""
Iterating means going through elements one by one.
As we deal with multi-dimensional arrays in numpy, we can do
    this using basic for loop of python.
If we iterate on a 1-D array it will go through each element one by one.
In a 2-D array it will go through all the rows.
In a 3-D array it will go through all the 2-D arrays.
"""
import numpy as np
"""
# Iterate on the elements of the following 1-D array:
arr = np.array([1, 2, 3])

for x in arr:
    print(x)
print(' ')


# Iterate on the elements of the following 2-D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print(x)
    for y in x:
        print(y)
print(' ')


# Iterate on the elements of the following 3-D array:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    print (x)
    for y in x:
        print(y)
        for z in y:
            print(z)
print(' ')
"""
"""
Iterating Arrays Using nditer()
In basic for loops, iterating through each scalar of an array we need to
    use n for loops which can be difficult to write for arrays with very
    high dimensionality.
To solve this problem, use Using nditer()
"""

# Iterate through the following 3-D array:
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)


"""
Iterating Array With Different Data Types
We can use op_dtypes argument and pass it the expected datatype to change the
    datatype of elements while iterating.
In order to enable it in nditer() we pass flags=['buffered'].
"""

arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags = ['buffered'], op_dtypes = ['S']):
    print(x)

# Iterate through every scalar element of the 2D array skipping 1 element:

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
    print(x)
