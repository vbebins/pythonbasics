'''
Syntax : try except else finally raise

try:
some code
except:
handle exception
else:
if no exception
finally:
always execute
raise => throw exception
'''

try:
    x=input("Enter x value:")
    print("Entered int is",int(x)/0)
except ZeroDivisionError:
    print("Divide by zero rule error")
except Exception as ex:
    print(ex.args)
