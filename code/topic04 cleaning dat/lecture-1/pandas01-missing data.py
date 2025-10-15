# code snippets for lectures
# Author: Andrew Beatty

import pandas as pd
# up two levels past topic04 and then down into data
datadir = "../../data/"
filename="people-100-dirty.csv"


df= pd.read_csv(datadir+filename)

# Detect missing values
print(df.isnull().sum())

# Drop rows with missing values
#df.dropna(inplace=True)

# Fill missing values
df.fillna(value='default_value', inplace=True)

# drop duplicate rows
df.drop_duplicates(inplace=True)
df.to_csv( "temp_file.csv")