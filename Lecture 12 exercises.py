# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 21:02:47 2024

@author: valie
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

x = range(300)
y = np.random.choice([-1, 0, 1], 300)
y = np.cumsum(y)

fig, ax = plt.subplots()
ax.plot(x, y, 'b-', label = 'my line')
ax.legend(loc='best')

# Add second axis

new_y = y[::-1] * 100
ax2 = ax.twinx()
ax2.plot(x, new_y, 'r-', label = 'my second line')
ax2.legend(loc='best')

# Second method to add the legend

fig, ax = plt.subplots()
ax.plot(x, y, 'b-', label = 'my line')
ax.plot(np.NaN, 'r-', label = 'my second line')
ax.legend(loc='upper center')
new_y = y[::-1] * 100
ax2 = ax.twinx()
ax2.plot(x, new_y, 'r-')

# Pandas can do the same thing automatically
df = pd.DataFrame({'values_y1':y, 'values_y2':new_y})
ax = df.plot(secondary_y = 'values_y2')


# Create a figure with multiple plot

fig, ax = plt.subplots(1, 2)
fig, ax = plt.subplots(2, 1)

fig, ax = plt.subplots(2, 2)
ax[0][1].plot(x, y, 'b-', label = 'my line')
ax[1][1].plot(y, x, 'r-', label = 'my line')

# Unpacking
fig, axs = plt.subplots(2, 1)
ax1, ax2 = axs

fig, axs = plt.subplots(2, 2)
(ax1, ax2), (ax3, ax4) = axs

# Pandas can do more subplots for us
df = pd.DataFrame({'values_y1':y, 'values_y2':new_y})
ax = df.plot(secondary_y = 'values_y2', subplots=True)

# Scatterplot
fig, ax = plt.subplots()
ax.plot(x, y, linestyle='', marker='.', markersize=5)

fig, ax = plt.subplots()
ax.scatter(x, y)

# barchart

a = [2, 4, 6, 8, 19]
b = [1., .2, .4, .7, .6]

fig, ax = plt.subplots()
ax.bar(a, b)

# Box plot
x = [np.random.normal(10, 2, 100),
   np.random.normal(11, 1, 100),
   np.random.normal(15, 4, 100)]

fig, ax = plt.subplots()
ax.boxplot(x)

# Using Seaborn for box plots

df = pd.DataFrame(np.array(x).T, columns=['first', 'second', 'third'])
df.head()

sns.set()
sns.boxplot(data=df)

# Group boxplots

tips = sns.load_dataset('tips')
tips.head()

ax = sns.boxplot(x = 'day', y='total_bill', hue='smoker',
                 palette =['r', 'b'], data=tips)