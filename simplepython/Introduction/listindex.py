#!/usr/bin/env python

list1 = ["The sorcer apprentice", "The day after tomorrow", "The jungle book", "Next three days", "Inception"]

print(type(list1))
print(len(list1))
print(list1)
print(list1[2])
print(list1[:])
print(list1[3:])

list2 = ["garbage1", "garbage2", "garbage3"]

list3 = [list1, list2]
print(list3)
print(len(list3))
print(list3[1][2])

print("The two string are : ", list1, list2)



