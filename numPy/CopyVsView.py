"""
The main difference between a copy and a view of an array is that the copy is
    a new array, and the view is just a view of the original array.
The copy owns the data and any changes made to the copy will not affect
    original array, and any changes made to the original array will not affect
    the copy.
The view does not own the data and any changes made to the view will affect the
    original array, and any changes made to the original array will affect
    the view.

"""

# Make a copy, change the original array, and display both arrays:
# The copy SHOULD NOT be affected by the changes made to the original array.


import numpy as np

arr = np.array([10, 20, 30, 40])

something = arr.copy()

arr[0] = 110

print(arr)
print(something)

# Make a view, change the original array, and display both arrays:
# The view SHOULD be affected by the changes made to the original array.

arr = np.array([1, 2, 3, 4, 5])
someThing = arr.view()
arr[0] = 100
print(arr)
print(someThing)



# Make a view, change the view, and display both arrays:
# The original array SHOULD be affected by the changes made to the view.

arr = np.array([100, 200, 300])
arr2 = arr.view()
arr2[0] = 500

print(arr)
print(arr2)

"""
As mentioned above, copies owns the data, and views does not own the data
Every NumPy array has the attribute 'base' that returns None if the array owns the data.
Otherwise, the base  attribute refers to the original object.
"""
# Print the value of the base attribute to check if an array owns it's
#   data or not:
# The copy returns None.
# The view returns the original array.

arr = np.array([20, 40, 60])

arrCopy = arr.copy()
arrView = arr.view()

print(arrCopy.base)
print(arrView.base)








































