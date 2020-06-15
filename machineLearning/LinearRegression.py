"""
The term regression is used when you try to find the relationship between
    variables.

In Machine Learning, and in statistical modeling, that relationship is used to
    predict the outcome of future events.

Linear regression uses the relationship between the data-points to draw a
    straight line through all them.

This line can be used to predict future values.

The r-squared value ranges from -1 to 1, where 0 means no relationship, and 1,
or -1, means 100% related.
"""
import matplotlib.pyplot as plt
from scipy import stats

# cars ages
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]

# cars speeds
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Execute a method that returns some important key values of Linear Regression:
slope, intercept, r, p, std_err = stats.linregress(x, y)

# check fot relationship
print(r) # there is a -0.76 relationship. Its a good fit for linear regression

# Create a function that uses the slope and intercept values to return
# a new value. This new value represents where on the y-axis the
# corresponding x value will be placed:
def myFunc(x):
    return slope*x+intercept

# Run each value of the x array through the function. This will result
# in a new array with new values for the y-axis:
yModel = list(map(myFunc, x))

# Draw the original scatter plot:
plt.scatter(x, y)

# Draw the line of linear regression:
plt.plot(x, yModel)

# Display the diagram:
plt.show()
