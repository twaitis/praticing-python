# We can create a NumPy ndarray object by using the array() function.
import numpy as np # this is the first step of creating an array


arr = np.array((1, 2, 3, 4, 5)) # we can pass a list or a tuple
print(arr)                      # and it will be converted into a ndarray
print(type(arr))

"""
A dimension in arrays is one level of array depth (nested arrays).
0-D arrays, or Scalars, are the elements in an array.
Each value in an array is a 0-D array.
"""
# Create a 0-D array with value 50
o_d_array = np.array(50)
print(o_d_array)

"""
An array that has 0-D arrays as its elements is called
uni-dimensional or 1-D array.
These are the most common and basic arrays.
"""

# Create a 1-D array containing the values 1,2,3,4,5:
D1_array = np.array([1, 2, 3, 4, 5])
print(D1_array)


"""
An array that has 1-D arrays as its elements is called a 2-D array.
These are often used to represent matrix or 2nd order tensors.
"""

# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
D_2_Array = np.array([[1, 2, 3],[1, 2, 3]])
print(D_2_Array)


"""
An array that has 2-D arrays (matrices) as its elements is called 3-D array.
These are often used to represent a 3rd order tensor.
"""

# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
D_3_array = np.array([[[1, 2, 3],[4, 5, 6]],[[1, 3, 4],[5, 6, 7]]])
print(D_3_array)


# NumPy Arrays provides the ndim attribute that returns an integer that tells us
# how many dimensions the array have.
# Check how many dimensions the arrays have:

print(D1_array.ndim)
print(D_2_Array.ndim)
print(D_3_array.ndim)


"""
An array can have any number of dimensions.
When the array is created, you can define the
number of dimensions by using the ndmin argument.
"""
# Create an array with 5 dimensions and verify that it has 10 dimensions:
arra = np.array([1, 2, 3, 4], ndmin = 10)

print(arra)
print('number of dimensions :', arra.ndim)
