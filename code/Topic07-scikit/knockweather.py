# a program to check if the mean wind at knock is affected by the month
# WARNING this is not the same data set from knock I asked you to look at in the 
# assignment

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("https://cli.fusio.net/cli/climate_data/webdata/mly4935.csv", skiprows=19)
#print(df.head(3))

corrtemp = df["month"].corr(df["meant"])
print(corrtemp)

# ok now lets look at the wind
cleandf = df[["month","wdsp"]]

# we need to clean the wind speeds of the blank data
cleandf['wdsp']= cleandf.loc[:,('wdsp')].replace(' ', np.nan)
cleandf.dropna(inplace=True)

# convert to float
cleandf['wdsp'] = cleandf['wdsp'].astype(float)

# is there a correlation?
corrwind = cleandf["month"].corr(cleandf["wdsp"])
print (f"wind correlation {corrwind}")

# not much lets do a regression
sns.set_style('whitegrid')
sns.lmplot(x='month', y='wdsp', order=3, data=cleandf)
plt.show()
