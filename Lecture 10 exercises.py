# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 22:51:24 2024

@author: valie
"""

import pandas as pd
import os

url_to_csv = r'N:\3 MES DOSSIERS SECONDAIRES\MASTER PREPARATION PROGRAM\University of Chicago\Academic Section\Course Materials\DAP I\MyGitHub\DAP_Ralph1558'

diamond_data = os.path.join(url_to_csv, 'diamonds.csv')
df = pd.read_csv(diamond_data )

df['cut'].unique()

df.mean(numeric_only=True)

df.groupby('cut')

mean_by_cut = df.groupby('cut').mean(numeric_only=True)
mean_by_cut

mean_by_clarity = df.groupby('clarity').mean(numeric_only=True).round(2)
mean_by_clarity

df.groupby('clarity').mean(numeric_only=True).round(1)

#slide 5
mean_by_clarity = df.groupby('clarity').mean(numeric_only=True).round(2).reset_index()
mean_by_clarity.sort_values('clarity') # Ascending approach

mean_by_clarity.sort_values('clarity', ascending=False) # Descending approach

clarity_order = ['I3', 'I2', 'I1', 'SI2', 'SI1', 'VS2', 
                 'VS1', 'VVS2', 'VVS1', 'IF', 'FL']

category = pd.Categorical(df_clarity['clarity'], 
                          categories=clarity_order, 
                          ordered=True)
category
mean_by_clarity['clarity'] = category
mean_by_clarity.sort_values('clarity')

#slide 11
df['>1ct'] = df['carat'].map(lambda c: 1 if c > 1 else 0)
df.groupby(['clarity', '>1ct']).mean(numeric_only=True).round(2) # Group by several category

#slide 14
grouped = df.groupby('clarity')
grouped

grouped.groups
df.iloc[15]

grouped.get_group('VVS1')
grouped.describe()
grouped.apply(lambda g: g['depth'].mean())
grouped.apply(lambda g: g['carat'].max())
grouped.apply(lambda g: g['price'].std())

#slide 21
df['cut'].str.upper()

df['cut'].str.replace('Ideal', 'Pretty OK I guess')

#slide 23
from numpy import NaN
data = {'col1':[NaN, 2, NaN, 4], 
        'col2':[NaN, 6, 7, 8], 
        'col3':[NaN, 10, 11, 12]}
df = pd.DataFrame(data)
df

df.dropna()
df.dropna(how='all')

df.dropna(axis=1, thresh=3)

df.fillna(0)
df.fillna(method='backfill')
df.fillna({'col1':100, 'col2':200, 'col3':300})

df['col1'].fillna(df['col2'])
df.iloc[0,:].fillna(df.iloc[1,:])

df.fillna(100, limit=1)
df.fillna(100, limit=3)

df.T
df.T.fillna(method='bfill', limit=1)
