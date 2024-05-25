from numpy import log, sqrt, NaN
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
import numpy as np

import numpy as np
from numpy import log, sqrt, NaN
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web

log(10**2)
2 * log(10)
log(1)
log(0)
log(-1)
np.log(10)

#slide 6
def ihs(x):
    return log(x + sqrt(x**2 + 1))

linear  = range(1, 11)

squared = [v**2 for v in linear]
logged  = [log(s) for s in squared]
ihsed = [ihs(s) for s in squared]

fig, axs = plt.subplots(2, 1)
axs[0].plot(linear, squared, 'g-', label='squared')
axs[0].plot(linear, linear, 'k--')
axs[1].plot(linear, linear, 'k--', label='linear')
axs[1].plot(linear, logged,  'b-', label='sq logged')
axs[1].plot(linear, ihsed, 'r-', label='sq ihs')
fig.legend(loc='upper center', ncol=2)
plt.show()
#slide 17
series = ['CPMNACSCAB1GQDE', 'LRUNTTTTDEQ156S',
          'CPMNACSCAB1GQPL', 'LRUNTTTTPLQ156S']
df = web.DataReader(series, 'fred', start='1995-01-01', end='2019-10-01')

df = df.rename({'CPMNACSCAB1GQDE':'GDPGermany',
                'LRUNTTTTDEQ156S':'EMPGermany',
                'CPMNACSCAB1GQPL':'GDPPoland',
                'LRUNTTTTPLQ156S':'EMPPoland'}, axis=1)
df = df.reset_index()

df_long = pd.wide_to_long(df, ['GDP', 'EMP'], i='DATE',
                                              j='COUNTRY',
                                              suffix='\\w+')

fig, ax = plt.subplots()
for label, d in df_long.reset_index().groupby('COUNTRY'):
    d.plot(x='DATE', y='GDP', label=label, ax=ax)
ax.legend()
ax.set_title('GDP')

model = smf.ols('GDPGermany ~ GDPPoland ', data=df)
result = model.fit()
result.summary()

#slide 21
df['Germany_GDP_lfd'] = log(df['GDPGermany']) - log(df['GDPGermany'].shift())
df['Poland_GDP_lfd']  = log(df['GDPPoland'])  - log(df['GDPPoland'].shift())

fig, ax = plt.subplots()
ax.plot(df['DATE'], df['Germany_GDP_lfd'], 'b-', label='Germany')
ax.plot(df['DATE'], df['Poland_GDP_lfd'], 'r-', label='Poland')
ax.legend()
ax.set_title('GDP')

model = smf.ols('Germany_GDP_lfd ~ Poland_GDP_lfd ', data=df)
result = model.fit()
result.summary()

#slide 25
g_cycle, g_trend = sm.tsa.filters.hpfilter(df['GDPGermany'], lamb=1600)
p_cycle, p_trend = sm.tsa.filters.hpfilter(df['GDPPoland'], lamb=1600)

fig, axs = plt.subplots(2, 1, figsize=(12,6))
axs[0].plot(g_cycle.index, g_cycle, 'b-', label='Germany')
axs[0].plot(g_cycle.index, p_cycle, 'r-', label='Poland')
axs[1].plot(g_trend.index, g_trend, 'b-')
axs[1].plot(g_trend.index, p_trend, 'r-')
axs[0].set_ylabel('Cycle')
axs[1].set_ylabel('Trend')
fig.legend(loc='upper center', ncols=2)
plt.show()

model = sm.OLS(g_cycle, sm.add_constant(p_cycle))
result = model.fit()
result.summary()

#slide 29
import numpy as np
def hamilton_filter(data, h=8, p=4):
    def _shift(orig_series, n):
        #implements efficient (positive) shifting for non-Series dtypes
        new_series = np.empty_like(orig_series)
        new_series[:n] = np.NaN
        new_series[n:] = orig_series[:-n]
        return new_series

    new_cols = [_shift(data, s) for s in range(h, h+p)]

    exog = sm.add_constant(np.array(new_cols).transpose())
    model = sm.GLM(endog=data, exog=exog, missing='drop')
    res = model.fit()

    trend = res.fittedvalues
    rand = data - _shift(data, h)
    cycle = res.resid_pearson
    return cycle, trend, rand

g_cycle, g_trend, _ = hamilton_filter(df['GDPGermany'])
p_cycle, p_trend, _ = hamilton_filter(df['GDPPoland'])

fig, axs = plt.subplots(2, 1, figsize=(12,6))
axs[0].plot(g_cycle.index, g_cycle, 'b-', label='Germany')
axs[0].plot(g_cycle.index, p_cycle, 'r-', label='Poland')
axs[1].plot(g_trend.index, g_trend, 'b-')
axs[1].plot(g_trend.index, p_trend, 'r-')
axs[0].set_ylabel('Cycle')
axs[1].set_ylabel('Trend')
fig.legend(loc='upper center', ncols=2)
plt.show()

g_cycle.name = 'Germany_hamilton'
p_cycle.name = 'Poland_hamilton'

model = sm.OLS(g_cycle, sm.add_constant(p_cycle))
result = model.fit()
result.summary()