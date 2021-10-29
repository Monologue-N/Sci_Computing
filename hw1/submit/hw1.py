import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import optimize

df = pd.DataFrame({'x': [4000.0000, 13500.000, 32000.000, 62500.000],
                   'y': [0.57101, 5.8720, 32.122, 121.95]})

logx = np.log10(df.x)
logy = np.log10(df.y)
A = np.vstack([logx, np.ones(len(logx))]).T
m, c = np.linalg.lstsq(A, logy, rcond = None)[0]
plt.plot(logx, logy, 'o', label='Original data', markersize=10)
plt.plot(logx, m * logx + c, 'r', label='Fitted line')
plt.xlabel('log(#_of_atoms)')
plt.ylabel('log(runtime(s))')
plt.title('log-log plot of T vs. N')
plt.legend()
plt.show()
print(m)
print(c)

xdata = np.array([4000.0000, 13500.000, 32000.000, 62500.000])
ydata = np.array([0.57101, 5.8720, 32.122, 121.95])

'''
# objective function
def objective(x, a, b)
	return a * x + b
'''