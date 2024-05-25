# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:18:57 2024

@author: valie
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = range(300)
y = np.random.choice([-1, 0, 1], 300)
y = np.cumsum(y)

fig, ax = plt.subplots()
ax.plot(x, y)

fig, ax = plt.subplots()
ax.plot(x, y, color='red', linestyle='dashed')

fig, ax = plt.subplots()
ax.plot(x, y, color='red', linestyle='solid')

fig, ax = plt.subplots()
ax.plot(x, y, color='red', linestyle='solid', marker='o', linewidth=2,
        markersize=5, markerfacecolor='red', markeredgecolor='black')

# Using shortcut for argumennt

fig, ax = plt.subplots()
ax.plot(x, y, 'r-')

fig, ax = plt.subplots()
ax.plot(x, y, 'k--')


fig, ax = plt.subplots()
ax.plot(x, y, 'r-', label='A red line')
ax.legend(loc='best')

fig, ax = plt.subplots()
ax.plot(x, y, 'r-', label='A red line')
ax.plot(x, y[::-1], 'b-', label='A blue line')
ax.legend(loc='best')
ax.set_ylabel('My first y plot')
ax.set_xlabel('My first x plot')
ax.set_title('My first plot title')

fig, ax = plt.subplots()
ax.plot(x, y, 'b-')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.axvline(150, color='k', linestyle=':')
ax.axhline(-7.5, color='k', linestyle=':')

# MatPlotLib and Pandas

df = pd.DataFrame({'value_x':x, 'value_y':y})
ax = df.plot(x='value_x', y='value_y')
ax.axvline(150, color='k', linestyle=':')








