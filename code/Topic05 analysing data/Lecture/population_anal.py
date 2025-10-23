# analysisng population wrong
# Author: Andrew Beatty

import pandas as pd 

FILENAME="population_for_analysis.csv"
DATADIR= "./"
FULLPATH =  DATADIR + FILENAME

df = pd.read_csv(FULLPATH)

#print (df.head(3))
headers = df.columns[1:]
print (headers)
district = headers[0]
print (df[district].describe())
print(df[district])
