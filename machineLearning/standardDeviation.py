"""
Standard deviation is a number that describes how spread out the values are.
A low standard deviation means that most of the numbers are close to the
    mean (average) value.
A high standard deviation means that the values are spread out over a wider
    range.

"""

# Use the NumPy std() method to find the standard deviation:

import numpy as np

speed = [86,87,88,86,87,85,86]

x = np.std(speed)

print(x)


"""
Variance is another number that indicates how spread out the values are.

In fact, if you take the square root of the variance, you get the standard
deviation!

Or the other way around, if you multiply the standard deviation by itself,
you get the variance!

To calculate the variance you have to do as follows:

1. Find the mean:
2. For each value: find the difference from the mean:
3. For each difference: find the square value:
4. The variance is the average number of these squared differences:
Luckily, NumPy has a method to calculate the variance:
"""
# Use the NumPy var() method to find the variance:

speed = [32,111,138,28,59,77,97]

x = np.var(speed)

print(x)

"""
Standard Deviation is often represented by the symbol Sigma: σ

Variance is often represented by the symbol Sigma Square: σ2
"""


















