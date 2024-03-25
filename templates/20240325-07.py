import datetime
import datetime as dt
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import time

x = dt.datetime.now()
print(x)
print(x.year, x.month, x.day, x.hour, x.minute, x.second, x.microsecond)
print(x.weekday())
print(x.strftime("%A %d. %B %Y"))
print(x.strftime("%H시 %M분 %S초"))
print(dt.datetime.strptime("2017-01-02 14:44", "%Y-%m-%d %H:%M"))

print(parse("2016-04-16"))

dt1 = datetime.datetime(2016, 2, 19, 14)
dt2 = datetime.datetime(2016, 1, 2, 13)
td = dt1 - dt2
print(td)

print(td.days)
print(td.seconds)
print(td.microseconds)
print(td.total_seconds())

t0 = datetime.datetime(2018, 9, 1, 13)
d = datetime.timedelta(days=90, seconds=3600)

print(t0 + d)

print(t0 + relativedelta(months=2))

print(1)

time.sleep(5)

print(2)

time.sleep(5)

print(3)

time.sleep(5)

print(4)