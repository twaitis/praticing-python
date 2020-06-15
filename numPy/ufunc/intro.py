"""
ufuncs stands for "Universal Functions" and they are NumPy functions that
    operates on the ndarray object.
ufuncs are used to implement vectorization in NumPy which is way faster than
    iterating over elements.
ufuncs also take additional arguments, like:

where boolean array or condition defining where the operations should take place.

dtype defining the return type of elements.

out output array where the return value should be copied.


What is Vectorization?
Converting iterative statements into a vector based operation is called
    vectorization.


"""
# add elements from both arrays
# Without ufunc, we can use Python's built-in zip() method:

x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
z = []

for i, j in zip(x, y):
    z.append(i+j)

print(z)

# NumPy has a ufunc for this, called add(x, y) that will produce the same result.
import numpy as np
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
z = np.add(x, y)
print(z)

