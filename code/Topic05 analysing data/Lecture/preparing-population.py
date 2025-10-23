# Preparing the population data for analysis
# The CSO data is quite clean 
# All we realy have to do is group it
# Author: Andrew Beatty

import pandas as pd 

FILENAME="cso-populationbyage.csv"
DATADIR= "../../data/"
FULLPATH =  DATADIR + FILENAME

df = pd.read_csv(FULLPATH)

drop_col_list = ["Statistic Label","CensusYear","Sex","UNIT"]
#df = df.drop(columns=drop_col_list)
df.drop(columns=drop_col_list, inplace=True)

df = df[df["Single Year of Age"] != "All ages"]
df["Single Year of Age"] = df["Single Year of Age"].str.replace('Under 1 year', '0')
df["Single Year of Age"] = df["Single Year of Age"].str.replace('\D', '', regex=True)

df['Single Year of Age']=df['Single Year of Age'].astype('int64')

#df_anal =pd.crosstab(df.loc[:, 'Administrative Counties'], df.loc[:, 'Single Year of Age'])
df_anal = pd.pivot_table(df, 'VALUE',"Single Year of Age","Administrative Counties")
print (df_anal.head(10))
df_anal.to_csv("population_for_analysis.csv")