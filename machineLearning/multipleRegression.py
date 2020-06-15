import pandas as pd
from sklearn import linear_model
"""
The Pandas module allows us to read csv files and return a DataFrame object.
"""

reader = pd.read_csv('cars.csv')

# Then make a list of the independent values and call this variable X.

# Put the dependent values in a variable called y.

X = reader[['Weight', 'Volume']]
y = reader['CO2']


regr = linear_model.LinearRegression()

regr.fit(X, y)

"""
Now we have a regression object that are ready to predict CO2 values based on a car's weight and volume:

"""
# predict the CO2 emission of a car where the weight is 2300kg, and
# the volume is 1300ccm:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)
