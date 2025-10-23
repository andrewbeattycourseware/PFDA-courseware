# weighted standard deviation

import pandas as pd
import numpy as number_people

FILENAME="population_for_analysis.csv"
DATADIR= "./"
FULLPATH =  DATADIR + FILENAME

df = pd.read_csv(FULLPATH)

#print (df.head(3))
headers = df.columns[1:]
print (headers)
district = headers[0]
# this is incorrect
print (df[district].describe())

import numpy as np
w_mean = np.average(df["Single Year of Age"], weights=df[district])
print(w_mean)

w_variance = np.average((df['Single Year of Age'] - w_mean) ** 2, weights=df[district])
w_standard_deviation = np.sqrt(w_variance)
print (w_standard_deviation)
