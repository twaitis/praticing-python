"""
To create you own ufunc, you have to define a function, like you do with
    normal functions in Python, then you add it to your NumPy ufunc library
    with the frompyfunc() method.

The frompyfunc() method takes the following arguments:
function - the name of the function.
inputs - the number of input arguments (arrays).
outputs - the number of output arrays.
"""

import numpy as np

# Create your own ufunc for addition:
def adder(x, y):
    return x+y
npadder = np.frompyfunc(adder, 2, 1)

print(npadder([1, 2, 3, 4], [1, 2, 3, 4]))
print(' ')
print(type(npadder))
print(' ')

# Use an if statement to check if the function is a ufunc or not:

if type(npadder)== np.ufunc:
    print('npadder is a Universal Function')
else:
    print('its not an ufunc')
    
