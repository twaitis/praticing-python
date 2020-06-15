"""
Reshaping means changing the shape of an array.
The shape of an array is the number of elements in each dimension.
By reshaping we can add or remove dimensions or change number of
    elements in each dimension.

"""

# Convert the following 1-D array with 12 elements into a 2-D array.
# The outermost dimension will have 4 arrays, each with 3 elements:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

arr_2D = arr.reshape(4, 3)

print(arr_2D)
print('Check it copy or view :', arr.reshape(4,3).base)
print('it is a view, because it did not return \'none\'')

# Convert the following 1-D array with 12 elements into a 3-D array.

# The outermost dimension will have 2 arrays that contains 3 arrays, each
# with 2 elements:

arr_3D = arr.reshape(2, 3, 2)
print(arr_3D)


"""
You are allowed to have one "unknown" dimension.
Meaning that you do not have to specify an exact number for one of the
    dimensions in the reshape method.
Pass -1 as the value, and NumPy will calculate this number for you.
Note: We can not pass -1 to more than one dimension.
"""

# Convert 1D array with 8 elements to 3D array with 2x2 elements:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
arr_3D = arr.reshape(2, 2, -1)
print(arr_3D)


"""
Flattening array means converting a multidimensional array into a 1D array.

We can use reshape(-1) to do this.
"""
# Convert the array into a 1D array:
arr_1D = arr_3D.reshape(-1)
print(arr_1D)



