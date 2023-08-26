class Person:
    def __init__(self):
        self.name="Bebins"

    def GetName(self):
        print("Your name is ", self.name)


p=Person()

print("Get name from the class object:", p.name)


#Inheritance: syntax childclass(parentclass)
class ChildPerson(Person):

    def GetChildName():
        print("Print Child Name")

c= ChildPerson()

print("Get name from the child class object:", c.name)
    

