import re
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
from datetime import datetime
import pytz

logFilename = './data/access.log'



def parse_str(x):
    """
    Returns the string delimited by two characters.

    Example:
        `>>> parse_str('[my string]')`
        `'my string'`
    """
    return x[1:-1]

def parse_datetime(x):
    '''
    Parses datetime with timezone formatted as:
        `[day/month/year:hour:minute:second zone]`

    Example:
        `>>> parse_datetime('13/Nov/2015:11:45:42 +0000')`
        `datetime.datetime(2015, 11, 3, 11, 45, 4, tzinfo=<UTC>)`

    Due to problems parsing the timezone (`%z`) with `datetime.strptime`, the
    timezone will be obtained using the `pytz` library.
    '''
    dt = datetime.strptime(x[1:-1], '%d/%b/%Y:%H:%M:%S')
    return dt
    #this log file does not have a timezone so I can ignore this issue 
    #dt_tz = int(x[-6:-3])*60+int(x[-3:-1])
    #return dt.replace(tzinfo=pytz.FixedOffset(dt_tz))


df = pd.read_csv(
    'data/access.log',
    sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
    engine='python',
    na_values='-',
    header=None,
    usecols=[0, 3, 4, 5, 6, 7, 8],
    names=['ip', 'time', 'request', 'status', 'size', 'referer', 'user_agent'],
    converters={'time': parse_datetime,
                'request': parse_str,
                'status': int,
                'size': int,
                'referer': parse_str,
                'user_agent': parse_str})


# informaation about the request
request = df.pop('request').str.split()
df['resource'] = request.str[1]
df['method'] = request.str[0]
#yes I could have used regex for this 
# from the request get the string before the ?
df['url'] = request.str[1].str.split('?').str[0] 

# I did this to look at the data
#excelFilename = './data/log.xlsx'
#df.to_excel(excelFilename, index=False, sheet_name='data')

dfbyhour=df.resample('H',on='time').sum()
# now we can extract the hours and dates
#df['time_of_day'] = df['time'].dt.time
# the index of this data frame is a datetime object
dfbyhour['hour'] = dfbyhour.index.hour
dfbyhour['date'] = dfbyhour.index.date
# now on to seaborn
#sns.lmplot(x="hour", y="size", order=5 ,data=dfbyhour, x_jitter=0.5)
sns.residplot(x="hour", y="size", data=dfbyhour, order=1)

plt.show()



