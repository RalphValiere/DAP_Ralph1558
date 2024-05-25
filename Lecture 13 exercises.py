import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

#slide 3
my_list  = [1, 2, 3, 4, 5]
my_array = np.array([1, 2, 3, 4, 5])

my_list*3
my_array*3

my_list + my_list
my_array + my_array

np.concatenate((my_array, my_array))

np.stack((my_array, my_array), axis=0)
np.stack((my_array, my_array), axis=1)

my_array.reshape(5, -1) #can use -1 instead of 5 to infer

np.array([1, 2, 'cat']) # That is for coercion!
np.array([1, True, 'cat'])

#slide 9 # About matrices
mat = np.array([[1, 2], [3, 4], [5, 6]])
mat

mat[0]
mat[1][1]
mat[1, 1]

mat.T # Finding the inverse of a matrix (columns to rows or rows to columns)
mat.dot(mat.T) # To multiply the matrix by another matrix
mat.dot(2) # Multiply by a constant.

np.linalg.pinv(mat)

mat.flatten() # Create a list out of a matrix!!
mat.dot(2).flatten()
mat.dot(mat.T).flatten()

#slide 13
df = sm.datasets.get_rdataset('Guerry', 'HistData').data
df.head()

#slide 14
x = df['Lottery']
y = df['Literacy']
m, b = np.polyfit(x, y, deg=1)
gen_lin1d = np.poly1d((m, b)) #creates a function which projects coeficients on other x values
# This is to create the projected value of x

fig, ax = plt.subplots()
ax.plot(x, y, 'ro')
ax.plot(x, gen_lin1d(x), 'k--')
ax.set_xlabel('Lottery')
ax.set_ylabel('Literacy')
ax.set_title('1830\'s France "Moral Statistics"')
plt.show()

#slide 18
model = smf.ols('Lottery ~ Literacy + Wealth', data=df)
result = model.fit()
model.fit().pvalues
model.fit().params
model.fit().rsquared_adj
model.fit().rsquared

rs = result.summary()
rs

result.pvalues
result.params
result.rsquared

#see the patys documentation: https://patsy.readthedocs.io/en/latest/quickstart.html
model = smf.ols('Lottery ~ Literacy + Wealth + C(Region)', data=df)
result = model.fit()
result.summary()

df['intercept'] = np.ones(len(df))
model = sm.OLS(endog=df['Lottery'], exog=df[['intercept', 'Literacy', 'Wealth']])
result = model.fit()
result.summary()

df = sm.add_constant(df)
model = sm.OLS(endog=df['Lottery'], exog=df[['const', 'Literacy', 'Wealth']])
result = model.fit()
result.summary()


mat = df[['const', 'Literacy', 'Wealth']].to_numpy()
mat
