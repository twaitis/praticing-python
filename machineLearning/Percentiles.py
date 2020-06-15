"""
Percentiles are used in statistics to give you a number that describes the
    value that a given percent of the values are lower than.
What is the 75. percentile? The answer is 43, meaning that 75% of the people
    are 43 or younger.
The NumPy module has a method for finding the specified percentile:

"""

# Use the NumPy percentile() method to find the percentiles:
import numpy as np

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = np.percentile(ages, 50)

print(x)

# What is the age that 90% of the people are younger than?

x = np.percentile(ages, 90)

print('90% of the people are younger than ', x)



