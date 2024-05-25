# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:22:05 2024

@author: valie
"""

# Lecture 7

import pandas

import pandas as pd

data = {'month': [1, 2, 3],
        'unemp_il':[5.6, 5.7, 5.8],
        'unemp_wi':[6.1, 6.0, 6.1],
        'gdp_il':[6, 6, 7],
        'gdp_wi':[4, 5, 4]}


df = pd.DataFrame(data)

df
df[1:3]

df.loc[[0,2],:]
df[['month', "gdp_il"]].iloc[[0, 2]]


df[['month', 'gdp_il']]


df[[c for c in df.columns if c.endswith('wi')]]

# To import the mean function to do operation over columns

import numpy as np

np.mean(df['unemp_il'])

df['month'].mean()


# Select by row now

df[1:]

df[1:2]

df[:3]


# Rename index

df.index = ["First", "Second", "Third"]

# Select by row names

df.loc[['First', 'Second']]

# select by index loc

df.loc[['First', 'Second'], ['month']]

df.iloc[[1, 2], [2, 3]]

# select all rows


df.loc[:, ['month']]

# Select all column

df.iloc[[1, 2],:]

# Create new column

df['gdp/unemp'] = df['gdp_il'] / df['unemp_il']

df[0:]

df.index



