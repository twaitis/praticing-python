"""
By default Python have these data types:
- strings - used to represent text data, the text is given under
    quote marks. eg. "ABCD"
- integer - used to represent integer numbers. eg. -1, -2, -3
- float - used to represent real numbers. eg. 1.2, 42.42
- boolean - used to represent True or False.
- complex - used to represent a number in
    complex plain. eg. 1.0 + 2.0j, 1.5 + 2.5j

Data Types in NumPy:
NumPy has some extra data types, and refer to data types with one
character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the
characters used to represent them.
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

The NumPy array object has a property called dtype that
    returns the data type of the array:
"""

# Get the data type of an array object:
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr.dtype)

# Get the data type of an array containing strings:
arr = np.array(['Computer Science', 'Data Science', 'Linguistics', 'Science'])
print(arr.dtype)


# We use the array() function to create arrays, this function can take an
# optional argument: dtype that allows us to define the expected data type
# of the array elements:

arr = np.array(['Sam', 'Mohamed', 'Ali'], dtype = 'S')
print(arr)
print(arr.dtype)


# Create an array with data type 4 bytes integer:
arr = np.array([1, 2, 3, 4], dtype = 'i4')
print(arr)
print(arr.dtype)

"""
arr = np.array(['a', '2', '3'], dtype='i')
this will raise an error

Converting Data Type on Existing Arrays:
The best way to change the data type of an existing array, is to
    make a copy of the array with the astype() method.
The astype() function creates a copy of the array, and allows you to
    specify the data type as a parameter.
The data type can be specified using a string, like 'f' for float, 'i' for
    integer etc. or you can use the data type directly like float for float and
    int for integer.

"""

# Change data type from float to integer by using 'i' as parameter value:
arr = np.array([1.2, 2.3, 3.4, 4.5])
converted_arr = arr.astype('i')

print(converted_arr)
print(arr.dtype)
print(converted_arr.dtype)

# change the datatype from int to string using 'string'
arr = np.array(['a', 1, 2, 3])
newarr = arr.astype('S')
print(newarr)
print(newarr.dtype)

# Change data type from integer to boolean:
arr = np.array([1, 0, 3, 4, 5])
newArr = arr.astype('bool')
print(newArr)
print(newArr.dtype)

















