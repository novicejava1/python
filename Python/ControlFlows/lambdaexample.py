#!/usr/bin/env python

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f)
print(f(0))
print(f(1))
print(f(20))

a = 10
b = 20

x = lambda a, b : a + b
print(x(a,b))

