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

