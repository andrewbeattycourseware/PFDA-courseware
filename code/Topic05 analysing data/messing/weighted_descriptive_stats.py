# Weighted basic descriptive statistics in pandas
# Author: Andrew Beatty

import pandas as pd

df = pd.read_csv("population_for_analysis.csv")
print(df.info())

headers = list(df.columns)[1:]
#print(headers) 
#print (df[headers[0]].mean)

district = headers[0]
# weighted mean
number_people = df[district].sum()
print(number_people)
cumlative_age = (df["Single Year of Age"]*df[district]).sum()
print (cumlative_age)

weighted_mean = cumlative_age/number_people
print (f"mean age in {district} is {weighted_mean:.1f} ")

# Weighted median

# the data is already sorted by age 
# df.sort_values('Single Year of Age', inplace=True)

cumsum = df[district].cumsum()
cutoff = df[district].sum() / 2.0
median = df['Single Year of Age'][cumsum >= cutoff].iloc[0]
print(f"weighted median of {district} is {median}")