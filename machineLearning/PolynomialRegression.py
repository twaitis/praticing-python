"""
If your data points clearly will not fit a linear regression (a straight line
through all data points), it might be ideal for polynomial regression.

Polynomial regression, like linear regression, uses the relationship between
the variables x and y to find the best way to draw a line through the data
points.


"""
import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# NumPy has a method that lets us make a polynomial model:
myModel = np.poly1d(np.ployfit(x, y, 3))
                    
# Then specify how the line will display, we start at position 1, and
# end at position 22:
myLine = np.linspace(1, 22, 100)
                    
# Draw the original scatter plot:
plt.scatter(x, y)
                    
# Draw the line of polynomial regression:
plt.plot(myLine, myModel(myLine))
                    
# Display the diagram:
plt.show()



