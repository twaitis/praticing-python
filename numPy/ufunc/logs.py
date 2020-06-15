# Use the log2() function to perform log at the base 2.

# Find log at base 2 of all elements of following array:

import numpy as np

arr = np.arange(1, 10)

print('based 2 log ', np.log2(arr))
print(' ')

# Find log at base 10 of all elements of following array:
print('based 10 log ', np.log10(arr))

"""
Use the log() function to perform log at the base e.
"""
# Find log at base e of all elements of following array:
print(' ')
print('log at based e \'natural log\' ', np.log(arr))


"""
Log at Any Base
NumPy does not provide any function to take log at any base, so we can use the
frompyfunc() function along with inbuilt function math.log() with two input
parameters and one output parameter:
"""
from math import log

anybase = np.frompyfunc(log, 2, 1)
print(' ')
print(anybase(1000, 10))
