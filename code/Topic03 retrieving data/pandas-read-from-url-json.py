# program that demonstrates that you can read data directly from an URL in pandas
# Author: Andrew Beatty
import pandas as pd

#url = "https://andrewbeatty1.pythonanywhere.com/books"

# other json example
# this one does not work easily
#url = "https://www.gov.uk/bank-holidays.json"
url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=wind_speed_10m,rain&past_days=3&forecast_days=1"
df = pd.read_json(url)



print (df.head(3))
