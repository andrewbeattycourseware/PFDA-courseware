# reading csv file with pandas
# Author: Andrew Beatty

FILENAME= "data.csv"
DATADIR = "../datafiles/"

import pandas
df = pandas.read_csv(DATADIR + FILENAME)
print(df)