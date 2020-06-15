"""
Array indexing is the same as accessing an array element.
You can access an array element by referring to its index number.
The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

"""
# Get the first element from the following array:
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 200])

print(arr[0])

# Get the second element from the following array.
print('The second element of the array is', arr[1])

# Get third and fourth elements from the following array and add them.
print(arr[2]+arr[3])

"""
To access elements from 2-D arrays we can use comma separated integers
representing the dimension and the index of the element.
"""
# Access the 2nd element on 1st dim:
arr_2D = np.array([[10, 20, 30],[40, 50, 60]])
print('the 2nd element on 1st dim:', arr_2D[0, 1])

# Access the 3rd element on 2nd dim:
print('the 3rd element on 2nd dim:', arr_2D[1, 2])


"""
To access elements from 3-D arrays we can use comma separated integers representing
the dimensions and the index of the element.
"""
# Access the third element of the first array of the second array:

arr_3D = np.array([[[10, 20, 30],[40, 50, 60]],[[70, 80, 90],[100, 110, 120]]])

print('the third element of the first array of the second array:', arr_3D[1, 0, 2])


# Use negative indexing to access an array from the end.
# Print the last element from the 2nd dim:
arr_2_D = np.array([[1, 2, 3],[4, 5, 6]])

print('the last element from the 2nd dim:', arr_2_D[1, -1])











