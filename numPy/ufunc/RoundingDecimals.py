"""
There are primarily five ways of rounding off decimals in NumPy:
truncation
fix
rounding
floor
ceil
"""

import numpy as np

# Remove the decimals, and return the float number closest to zero.
# Use the trunc() and fix() functions.

arr = np.fix([-1.333, 1.333])
arr1 = np.trunc([-1.333, 1.333])

print(arr)
print(arr1)

# The around() function increments preceding digit or decimal by 1 if >=5
# else do nothing.

arr = np.around([1.333, 2.373], 1)

print(arr)
print(' ')

# The floor() function rounds off decimal to nearest lower integer.

arr = np.floor([-1.333, 2.373])
print(arr)
print(' ')





