# program showing how to read csv from a url using Pandas
# Author: Andrew Beatty

import pandas as pd

url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=wind_speed_10m,rain&past_days=3&forecast_days=1&format=csv"

# or a different protocol (you will need to pip instal S3fs)
#url = "s3://noaa-gsod-pds/2020/72278023183.csv"

df = pd.read_csv(url)
print (df.head)