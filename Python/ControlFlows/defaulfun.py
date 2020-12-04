#!/usr/bin/env python

def msgs(msg1, msg2="This is default message 2", msg3="This is default message 3"):
    print(msg1, msg2, msg3)

msgs("Actual Message")
msgs("This is binary", "This is hexa", "this is Octa")
