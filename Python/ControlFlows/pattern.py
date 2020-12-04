#!/usr/bin/env python

def series(a,b):
    """ This is pattern1 function """
    for i in range(a):
        for b in range(i):
            print("*", end="")
        print("")

series(10,10)

