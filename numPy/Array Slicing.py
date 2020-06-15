"""
Slicing in python means taking elements from one given index
to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1
"""

# Slice elements from index 2 to index 6 from the following array:
# Note: The result includes the start index, but excludes the end index.

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print(arr[2:6])


# Slice elements from index 4 to the end of the array:
print(arr[4:])

# Slice elements from the beginning to index 4 (not included):
print(arr[:4])

"""
Negative Slicing
Use the minus operator to refer to an index from the end:
"""

# Slice from the index 3 from the end to index 1 from the end:
print(arr[-3:-1])

"""
Use the step value to determine the step of the slicing:
"""
# Return every other element from index 0 to index 9:
print(arr[0:9:2])

# Return every other element from the entire array:
print(arr[::2])

"""
Slicing 2-D Arrays
"""
# From the second element, slice elements from index 1 to
# index 4 (not included):

arr_2d = np.array([[10, 20, 30, 40, 50],[60, 70, 80, 90, 100]])
print(arr_2d[1, 1:4])

# From both elements, return index 3:
print(arr_2d[0:2, 3])

# From both elements, slice index 1 to index 4 (not included),
# this will return a 2-D array:
print(arr_2d[0:2, 1:4])








