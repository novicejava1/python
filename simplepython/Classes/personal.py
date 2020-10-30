#!/usr/bin/env python

class Personal:

    def __init__(self, first, middle, sur, age, address):
        self.firstName = first
        self.middleName = middle
        self.surName = sur
        self.Age = age
        self.Address = address

    def __repr__(self):
        return '[Person: %s, %s, %s, %s, %s]' % (self.firstName, self.middleName, self.surName, self.Age, self.Address)

    def getfirstName(self):
        return self.firstName

    def getmiddleName(self):
        return self.middleName
    
    def getsurName(self):
        return self.surName
    
    def getAge(self):
        return self.Age
    
    def getAddress(self):
        return self.Address

