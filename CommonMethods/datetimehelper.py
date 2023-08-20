import datetime
from datetime import  timedelta

def SetExpiryInMinutes(x):
    return datetime.datetime.now()+timedelta(minutes=x)