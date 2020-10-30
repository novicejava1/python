#!/usr/bin/env python

import shelve
from personal import Personal

# Instantiate Person Objects 

p1 = Personal("Mike", "T", "Savii", "24", "Brook Street")
p2 = Personal("Jerry", "J", "Ros", "34", "Province Street")
p3 = Personal("Brad", "L", "Lore", "54", "Chench Street")

print(p1.firstName + " " + p1.middleName + " " + p1.surName + " " + p1.Age + " " + p1.Address)
print(p2.firstName + " " + p2.middleName + " " + p2.surName + " " + p2.Age + " " + p2.Address)
print(p3.firstName + " " + p3.middleName + " " + p3.surName + " " + p3.Age + " " + p3.Address)


db = shelve.open('persondb')

for obj in (p1, p2, p3):
    db[obj.firstName] = obj

db.close()

