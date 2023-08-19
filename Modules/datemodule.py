import datetime

now=datetime.datetime.now() 

'''
dir() - used to get list of props and methods of a module 
'''
print (dir(datetime))

#ciurrent date and time
print(now)

# date of today; only date
print(datetime.date.today())

#date object to represent a date
dt=datetime.date(2023,8,19)
print(dt)

#to import only date class
from datetime import date

todaydate=date.today()
print(todaydate)
#to get only day, month, year
print(todaydate.day)
print(todaydate.month)
print(todaydate.year)

from datetime import time

print(time())

#to get the current time
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
