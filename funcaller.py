from Modules import userdefinedfuneg
from CommonMethods.datetimehelper import DateTimeHelper
import sys


print("Sum of two values",userdefinedfuneg.AddNumbers(10,15))

print("Enter expiry value in Minutes:")

datefun=DateTimeHelper

print("Expiry Time is ",datefun.SetExpiryInMinutes(int(sys.stdin.readline())))