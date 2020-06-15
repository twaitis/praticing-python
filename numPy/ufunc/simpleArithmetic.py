"""
All of the discussed arithmetic functions take a where parameter in which
    we can specify that condition.
"""

import numpy as np

# The add() function sums the content of two arrays, and return the results in
# a new array.

# The subtract() function subtracts the values from one array with the values
# from another array, and return the results in a new array.

# The multiply() function multiplies the values from one array with the values
# from another array, and return the results in a new array.

# The divide() function divides the values from one array with the values from
# another array, and return the results in a new array.

# The power() function rises the values from the first array to the power of
# the values of the second array, and return the results in a new array.

# Both the mod() and the remainder() functions return the remainder of the
# values in the first array corresponding to the values in the second array,
# and return the results in a new array.

# The divmod() function return both the quotient and the the mod. The return
# value is two arrays, the first array contains the quotient and second
# array contains the mod.

# Both the absolute() and the abs() functions functions do the same absolute
# operation element-wise but we should use absolute() to avoid confusion
# with python's inbuilt math.abs()


arr1 = np.array([10, 20, 30])
arr2 = np.array([2, 2, 2])

added = np.add(arr1, arr2)
print('array added ', added)

subtracted = np.subtract(arr1, arr2)
print('array subtracted ', subtracted)

multiplied = np.multiply(arr1, arr2)
print('array multiplied ', multiplied)

divided = np.divide(arr1, arr2)
print('array division ', divided)

powerOf = np.power(arr1, arr2)
print('array power ', powerOf)

remainder = np.mod(arr1, arr2)
print('The remainder ', remainder)

divAndMod = np.divmod(arr1, arr2)
print('The division and remainder ', divAndMod)

