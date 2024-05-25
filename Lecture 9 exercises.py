# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 22:10:31 2024

@author: valie
"""

import pandas as pd

data = {'name':['a', 'b', 'c'], 'val1':[1, 2, 3]}

df1 = pd.DataFrame(data)

df1


data2 = {'name':['b', 'c', 'd'], 'val1':[4, 5, 6]}


df2 = pd.DataFrame(data2)

df2

df3 = df1.merge(df2, on="name", how='outer')

df4 = df1.merge(df2, on="name", how='inner')

df5 = df1.merge(df2, on="name", how='right')

df6 = df1.merge(df2, on="name", how='left')

df3
df4
df5
df6


data3 = {'name':['a', 'a', 'd'], 'val1':[7, 8, 9]}

df7 = pd.DataFrame(data3)


df8 = df1.merge(df7, on='name', how='left')

df8 # There is error while merging this data frame...


# How to correct it

df8 = df1.merge(df7, on='name', how='left', validate='1:1')

df8

# How to use the function assert()


x = 10
assert(x > 20), 'The variable is too little'
x = 14 # That code will not run until the condition is satisfied.


# Another example

x = [1, 3, 4, 2, 5, 5]
assert(len(x) == 5), 'The list doesnt have 5 entries'
# The code is not going to run as len(x) greater than 5

# Let's apply that to the merge
startlen = len(df1)
df8 = df1.merge(df7, on='name', how='left')
endlen = len(df8)

assert(startlen == endlen), 'There was an error while merging'

# We can use indicator argument to check too

df8 = df1.merge(df7, on='name', how='outer', indicator=True)
df8

df8 = df1.merge(df7, on='name', how='inner', indicator=True)
df8

df8 = df1.merge(df7, on='name', how='left', indicator=True)
df8

df8 = df1.merge(df7, on='name', how='right', indicator=True)
df8

df8['_merge']
df8.dtypes


# Now, how to do anti-join
df8[df8['_merge'] != 'both']

# Merge with different merge keys

data4 = {'NAMES':['a', 'b', 'c'], 'val1':[10, 11, 12]}

df9 = pd.DataFrame(data4)

df10 = df1.merge(df9, left_on='name', right_on='NAMES', how='inner')

df10

# Merge on multiple keys

data5 = {'name':['a', 'b', 'c', 'd'], 'month':[1, 6, 1, 6] ,'val_1':[13, 14, 15, 16]}

df11 = pd.DataFrame(data5)


data6 = {'name':['a', 'b', 'c', 'd'], 'month':[1, 6, 1, 6] ,'val_2':[17, 18, 19, 20]}

df12 = pd.DataFrame(data6)

df11.merge(df12, on=['name', 'month'], how='inner')

# Merge with concat method

pd.concat([df11, df12])

# Using concat but by making it wider or longer
pd.concat([df11, df12], axis=0) # longer

new_df = pd.concat([df11, df12], axis=1) # wider
new_df

# Re-shaping data frame (wide to long) using "stubnames"

new_df2 = pd.wide_to_long(new_df.iloc[:,[0, 2, 5]], stubnames='val_', i='name', j='index')

new_df2

new_df2 = new_df2.reset_index() # To insert an index column

new_df2

# Re-shaping data frame (wide to long) using "melt"


new_df3 = new_df.iloc[:,[0, 2, 5]].melt(id_vars="name", value_vars=None, var_name='index', value_name='value')
new_df.iloc[:,[0, 2, 5]]
new_df3

# Now, let reshape data frame (long to wide to long) using "pivot"

new_df4 = new_df3.pivot(index="name", columns='index', values='value')

new_df4
