from Modules import userdefinedfuneg
from CommonMethods import datetimehelper
import sys


print("Sum of two values",userdefinedfuneg.AddNumbers(10,15))

print("Enter expiry value in Minutes:")

datefun=datetimehelper

print("Expiry Time is ",datefun.SetExpiryInMinutes(int(sys.stdin.readline())))