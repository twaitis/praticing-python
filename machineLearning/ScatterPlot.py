"""
A scatter plot is a diagram where each value in the data set is represented by
a dot.

The Matplotlib module has a method for drawing scatter plots, it needs two
arrays of the same length, one for the values of the x-axis, and one for the
values of the y-axis:
"""
"""
# create an array 'x' to represents the ages of cars
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]

# create an array 'y' to represents the speeds of cars
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Use the scatter() method to draw a scatter plot diagram for x and y:
import matplotlib.pyplot as plt

plt.scatter(x, y)

# plt.show()
"""
"""
In Machine Learning the data sets can contain thousands-, or even millions,
of values.

You might not have real world data when you are testing an algorithm, you
might have to use randomly generated values.

Let us create two arrays that are both filled with 1000 random numbers from
a normal data distribution.

The first array will have the mean set to 5.0 with a standard deviation of 1.0.

The second array will have the mean set to 10.0 with a standard deviation of 2.0

and create a plot for both arrays

expectations:

We will see that the dots are concentrated around the value 5 on the x-axis,
and 10 on the y-axis.

We will also see that the spread is wider on the y-axis than on the x-axis.
because the standard deviation is hight on the y-axis
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)

plt.show()
























