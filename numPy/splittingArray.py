"""
Splitting NumPy Arrays
Splitting is reverse operation of Joining.
We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
"""
# Split the array in 4 parts:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

arrays = np.array_split(arr, 4)

print(arrays)
print(' ')
print(arrays[0])
print(arrays[1])
print(arrays[2])


print(' ')

# Split the 2-D array into three 2-D arrays.

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print(newarr)

# In addition, you can specify which axis you want to do the split around.

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
arr2 = np.array_split(arr, 3, axis = 1)
print(arr2)

# Use the hsplit() method to split the 2-D array into three 2-D arrays along rows.

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarray = np.vsplit(arr, 3)
print(newarray)
