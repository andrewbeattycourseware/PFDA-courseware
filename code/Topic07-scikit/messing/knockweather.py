# a program to check if the mean temperature at knock is affected by the month
# WARNING this is not the same data set from knock I asked you to look at in the 
# assignment

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("https://cli.fusio.net/cli/climate_data/webdata/mly4935.csv", skiprows=19)
print(df.head(3))

corrtemp = df["month"].corr(df["meant"])
print(corrtemp)

#print(df["wdsp"])

cleandf = df[["month","wdsp"]]
# pandas does not recognise the '' as an NA so I am converting them to na before droping them
#cleandf['wdsp'].replace('', np.nan, inplace=True)
# that did not work, I spent a while bashing my head to try and get this to work
# for some reason I could not get regex to work
# I searched and found
# https://stackoverflow.com/questions/29314033/drop-rows-containing-empty-cells-from-a-pandas-dataframe
# cleandf[cleandf['wdsp'].str.strip().astype(bool)] 
# and this did not work for me
# look at the offending value
# print(f"###{cleandf.loc[1,('wdsp')]}###")


# eventualy 
cleandf['wdsp']= cleandf.loc[:,('wdsp')].replace(' ', np.nan)
cleandf.dropna(inplace=True)

cleandf['wdsp'] = cleandf['wdsp'].astype(float)
print(cleandf.head(3))
corrwind = cleandf["month"].corr(cleandf["wdsp"])
print (f"wind correlation {corrwind}")
# not much lets do a regression
sns.set_style('whitegrid')
#sns.scatterplot(x='total_bill',y='tip',data=dataset)
sns.lmplot(x='month', y='wdsp', order=3, data=cleandf)
plt.show()
