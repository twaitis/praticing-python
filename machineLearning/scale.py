"""
The standardization method uses this formula:
z = (x - u) / s
Where z is the new value, x is the original value, u is the mean and s is the
    standard deviation.

You do not have to do this manually, the Python sklearn module has a method
called StandardScaler() which returns a Scaler object with methods for
transforming data sets.
"""
# Scale all values in the Weight and Volume columns:

import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

# reading the data file
df = pd.read_csv('cars.csv')

X = df[['Weight', 'Volume']]
y = df['CO2']

scaled_X = scale.fit_transform(X)

print(scaled_X)

# Predict the CO2 emission from a 1.3 liter car that weighs 2300 kilograms:

regr = linear_model.LinearRegression()
regr.fit(scaled_X, y)

scaled = scale.transform([[2300, 1.3]])

predCOS2 = regr.predict([scaled[0]])

print(predCOS2)
