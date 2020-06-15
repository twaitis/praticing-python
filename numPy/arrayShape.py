"""
The shape of an array is the number of elements in each dimension.
NumPy arrays have an attribute called shape that returns a tuple with
    each index having the number of corresponding elements.
"""

# Print the shape of a 3-D array:
import numpy as np

arr = np.array([[1, 2, 3],[4, 5, 6]])

print(arr.shape)

# it returns (2, 3), which means 2 dimentions and 3 elements in each


# Create an array with 5 dimensions using ndmin using a vector with
# values 1,2,3,4 and verify that last dimension has value 4:

arr = np.array([1, 2, 3, 4], ndmin = 5)
print(arr)
print('The shape of the array :', arr.shape)
