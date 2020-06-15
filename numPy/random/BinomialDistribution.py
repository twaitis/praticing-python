"""
Binomial Distribution is a Discrete Distribution.
It describes the outcome of binary scenarios, e.g. toss of a coin,
    it will either be head or tails.
n - number of trials.

p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).

size - The shape of the returned array.
"""

"""
Discrete Distribution:The distribution is defined at separate set of events,
    e.g. a coin toss's result is discrete as it can be only head or tails
    whereas height of people is continuous as it can be 170, 170.1, 170.11 and
    so on.
"""

# Given 20 trials for coin toss generate 10 data points:

import numpy as np
from numpy import random
import seaborn as sns


x = random.binomial(n = 10, p = 0.5, size = 10)

print(x)

# Visualization of Binomial Distribution

import matplotlib.pyplot as plt
"""
sns.distplot(random.binomial(n=10, p =0.5, size=1000), hist=True, kde = False)

plt.show()
"""

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='Normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='Binomial')

plt.show()
