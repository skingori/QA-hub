from datetime import datetime, timedelta
dt = datetime.utcnow()
from datetime import date
today = date.today()
import os
# print(today)
td = timedelta(days=-10)
# your calculated date
my_date = dt + td

# xtime = my_date.strftime("%Y-%m-%d")
#
# rtime = dt.strftime("%Y-%m-%d")
#
# print(xtime, rtime)

# convert to milliseconds

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds()


print(int(unix_time_millis(dt)))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(BASE_DIR)

print(os.path.join(BASE_DIR,'logs'))




