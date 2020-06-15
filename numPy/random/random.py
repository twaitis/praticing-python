import numpy as np
from numpy import random

# Generate a random integer from 0 to 500:
x = random.randint(500)

print(x)

# The random module's rand() method returns a random float between 0 and 1.
x = random.rand()

print(' ')
print(x)
print(' ')

# Generate a 1-D array containing 5 random integers from 0 to 5000:
x = random.randint(5000, size =(10))
print(x)
print(' ')

# Generate a 2-D array with 3 rows, each row containing 4 random integers
# from 0 to 100:

x = random.randint(100, size=(3, 5))
print(' ')


# Generate a 2-D array with 3 rows, each row containing 5 random numbers:
x = random.rand(3, 5)
print(x)
print(' ')

# The choice() method allows you to generate a random value based on an
# array of values.
x = random.choice([1, 2, 3, 4])
print(x)
print(' ')

# Add a size parameter to specify the shape of the array.
x = random.choice([1, 2, 3, 4], size=(2, 3))
print(x)
print(' ')





