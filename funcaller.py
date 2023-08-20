from Modules import userdefinedfuneg
from CommonMethods import datetimehelper
import sys


print("Sum of two values",userdefinedfuneg.AddNumbers(10,15))

print("Enter expiry value in Minutes:")

print("Expiry Time is ",datetimehelper.SetExpiryInMinutes(int(sys.stdin.readline())))