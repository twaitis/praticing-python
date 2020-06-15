"""
In the real world, the data sets are much bigger, but it can be difficult to
gather real world data, at least at an early stage of a project.

How Can we Get Big Data Sets?
To create big data sets for testing, we use the Python module NumPy, which
    comes with a number of methods to create random data sets, of any size.
"""

# Create an array containing 250 random floats between 0 and 5:

import numpy as np

x = np.random.uniform(0.0, 5.0, 250)

# print(x)

"""
To visualize the data set we can draw a histogram with the data we collected.

We will use the Python module Matplotlib to draw a histogram:

"""

# Draw a histogram:

import matplotlib.pyplot as plt

plt.hist(x, 5)

#plt.show()

# Create an array with 100000 random numbers, and display them using a
# histogram with 100 bars:

x = np.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)

plt.show()


