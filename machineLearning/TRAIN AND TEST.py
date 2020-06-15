"""
Train/Test is a method to measure the accuracy of your model.

It is called Train/Test because you split the the data set into two sets:
a training set and a testing set.

80% for training, and 20% for testing.

You train the model using the training set.

You test the model using the testing set.

Train the model means create the model.

Test the model means test the accuracy of the model.
"""
"""
Start With a Data Set
Start with a data set you want to test.

Our data set illustrates 100 customers in a shop, and their shopping habits.

The x axis represents the number of minutes before making a purchase.

The y axis represents the amount of money spent on the purchase.
"""
import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

# split into Train/Test

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

# Display the Training Set
plt.scatter(train_x, train_y)
plt.show()

# Draw a polynomial regression line through the data points:

mymodel = numpy.ployld(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()
























