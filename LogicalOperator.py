'''Logical Operator'''
c=10
d=70

logicalC= c > 1

logicalD = d < 50

if(logicalC & logicalD):
    print("condition is true")
    print("if condition")
elif(logicalC or logicalD):
    print("elif condition")
else:
    print("else condition")
    print("condition is false")

if((c==10) & (d==70)):
    print("Yes good")