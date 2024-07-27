## Dates

import datetime
from datetime import datetime
print("****** datetime ******")
now = datetime.now()
def printDate(date):
    print(now)
    print(now.date())
    print(now.ctime())
    print(now.day)
    print(now.month)
    print(now.year)
    print(now.hour)
    print(now.minute)
    print(now.second)
    print(now.timestamp())

newDate = datetime(2024,2,3)
print(newDate)

printDate(now)

from datetime import time

print("****** time ******")
current_time = time(15,5,3)
print(current_time.hour, current_time.minute, current_time.second)


from datetime import date

print("****** date ******")
current_date = date.today()
print(current_date)
print(current_date.day, current_date.month, current_date.year)
now = datetime.now()

from datetime import timedelta
start_timedelta = timedelta(200,100,100, weeks = 10)
end_timedelta = timedelta(300,100,100, weeks = 13)
print(end_timedelta - start_timedelta)

