# demonstration of basic standard deviation
# Author: Andrew Beatty

import pandas as pd

# create series
temp1 = pd.Series([56, 65, 78, 86, 88, 92])
temp2 = pd.Series([33, 65, 78, 88, 92, 109000])

# print mean and standard deviation
print(f'temp1: mean = {temp1.mean()}, standard deviation: {temp1.std()}')
print(f'temp2: mean = {temp2.mean()}, standard deviation: {temp2.std()}')