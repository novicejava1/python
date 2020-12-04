#!/usr/bin/env python

list1 = ["Bluffmaster", "Aankeen", "Inception", "The king kong"]

for item in list1:
    print(item, len(item))

for item in list1[:]:
    print(item, len(item))

for i in range(20,50,5):
    print(i, end=":")

print("Type of Range Object :", range(2,2))
print(list(range(2,2)))
