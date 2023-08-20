import datetime
from datetime import  timedelta

class DateTimeHelper:   
    def SetExpiryInMinutes(x):
        return datetime.datetime.now()+timedelta(minutes=x)