# program that reads in the meteo data correctly
# Author: Andrew Beatty

import pandas as pd

url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=wind_speed_10m,rain&past_days=3&forecast_days=1&format=csv"

df = pd.read_csv(url, header= 2)
print (df.head(3))
print (df.info())