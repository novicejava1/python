#!/usr/bin/env python

a, b = 0,1

while a < 20:
    print(a, end=':')
    a, b = b, a + b
print("\n")
print("End of Series")

