"""
Sorting means putting elements in a ordered sequence.
Ordered sequence is any sequence that has an order corresponding to elements,
    like numeric or alphabetical, ascending or descending
The NumPy ndarray object has a function called sort(), that will sort a
    specified array.
"""

import numpy as np

# Sort the array:
arr = np.array([4, 2, 5, 3, 1, 0])

print(np.sort(arr))

"""
Note: This method returns a copy of the array, leaving the original
array unchanged.
"""

arr = np.array(['Sam', 'Mohamed', 'Ali', 'Twaiti'])
print(np.sort(arr))

# Sort a boolean array:
arr = np.array([True, False, True])
print(np.sort(arr))

# If you use the sort() method on a 2-D array, both arrays will be sorted:

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))
