#!/usr/bin/env python

class Personal:
    firstName = "Sudhir"
    middleName = "Surendra"
    surName = "Bhoga"
    Age = 36
    Address = "BhumiRaj Woods CHS, Kharghar"

    def __init__(self, first, middle, sur, age, address):
        self.firstName = first
        self.middleName = middle
        self.surName = sur
        self.Age = age
        self.Address = address

    def getfirstName(self):
        print("Inside FirstName function")
        return self.firstName
    def getmiddleName(self):
        print("Inside MiddleName function")
        return self.middleName
    def getsurName(self):
        print("Inside Surname function")
        return self.surName
    def getAge(self):
        print("Inside Age funtion")
        return self.Age
    def getAddress(self):
        print("Inside Address function")
        return self.Address

# Instantiate an Object

#person1 = Personal()
person1 = Personal("Mike", "Taveras", "Johnson", 35, "Amber street")
#print(person1.firstName)
print(person1.getfirstName())
print(person1.getmiddleName())
print(person1.getsurName())
print(person1.getAge())
print(person1.getAddress())

