# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 00:34:02 2024

@author: valie
"""


data = {'month': [1, 2, 3],
        'unemp_il':[5.6, 5.7, 5.8],
        'unemp_wi':[6.1, 6.0, 6.1],
        'gdp_il':[6, 6, 7],
        'gdp_wi':[4, 5, 4]}

import pandas as pd

data = pd.DataFrame(data)

data.loc[[1, 2],['month', 'gdp_il']]


print('Manman t ap bat mwen\nsan kontwol wi')


# file path

import os

base_path = r'N:\3 MES DOSSIERS SECONDAIRES\MASTER PREPARATION PROGRAM\University of Chicago\Academic Section\Course Materials\DAP I\MyGitHub\DAP_Ralph1558'

path = os.path.join(base_path, 'GDPC1.csv')

df = pd.read_csv(path)

# Exploring the data frame...

df.tail

df.head

df.shape

# find data types
df.dtypes

# Example with date
# This is changing the DATE object which was a string as a object with the format datetime...
df['DATE 2'] = pd.to_datetime(df['DATE'])

# Ohter methode

df = pd.read_csv(path, parse_dates=['DATE'])

df
df.dtypes


# Renaming 

new_name = {'DATE':'Jou/Mwa', 'GDPC1':'riches'}

df = df.rename(new_name, axis=1) # Argument axis tells Python to give a result work accros row (0) or column (1)
# Working accross rows will give you a column, vice-versa


df = df.rename(columns = new_name)

# Subset by conditional

df[df['riches'] > 1000]


import datetime


start_date = datetime.datetime(1999, 1, 1)

df[df['Jou/Mwa'] > start_date]


df[(df['Jou/Mwa'] > start_date) & (df['riches'] > 1000)]


X = 'a'

X * 10


# Passing function to the data frame using map (for one value)

def some_math(x):
    return x * 2


df['riches'].map(some_math)
df['riches'].map(lambda x: x * 2)


# Passing function to the data frame using apply (accross the entire data set)

df['riches'].apply(lambda x: x * 2)

df

df[].apply(some_math)




