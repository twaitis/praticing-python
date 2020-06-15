"""
What is the difference between summation and addition?

Addition is done between two arguments whereas summation happens over n elements

"""

import numpy as np

arr1 = np.array([10, 20])
arr2 = np.array([30, 40])

# adding
adding = np.add(arr1, arr2)

#summing

summing = np.sum([arr1, arr2])

print(adding)
print(' ')
print(summing)

# If you specify axis=1, NumPy will sum the numbers in each array.

summinAxis = np.sum([arr1, arr2], axis=1)
print(' ')
print(summinAxis)

"""
Cummulative sum means partially adding the elements in array.

E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].

Perfom partial sum with the cumsum() function.
"""

arr = np.array([1, 1, 1])
newArray = np.cumsum(arr)
print(' ')
print(newArray)







