"""
Enumeration means mentioning sequence number of somethings one by one.
Sometimes we require corresponding index of the element while iterating,
    the ndenumerate() method can be used for those usecases.
"""

import numpy as np

arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
    

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
    
