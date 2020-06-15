"""
Visualize Distributions With Seaborn
Seaborn is a library that uses Matplotlib underneath to plot graphs.
It will be used to visualize random distributions.
"""

"""
Distplots
Distplot stands for distribution plot, it takes as input an array and
    plots a curve corresponding to the distribution of points in the array.

"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Plotting a Displot
"""
sns.distplot([0, 1, 2, 3, 4, 5])

plt.show(sns)
"""

# without the histogram

sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()
