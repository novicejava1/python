#!/usr/bin/env python

class greet:
    #print("Hello Greeting!!")
    def getMessage(self):
        return "Welcome to Python Class"

class student(greet):

    def getMessage(self):
        return "Welcome to Python Django Class"

    def greetStudent(self, name):
        return "Hello : " + name + " " + self.getMessage()



print("Executing the main section")
s1 = student()
s2 = student()

print(s1.greetStudent("Laura"))
print(s2.greetStudent("William"))

#g1 = greet()
#g2 = greet()

#print(type(greet))
#print(type(g1))

#print(g1.getMessage("Good Morning"))
#print(g2.getMessage("Good Afternoon"))


