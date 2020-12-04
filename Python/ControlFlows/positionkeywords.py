#!/usr/bin/env python

def posfun(*args):
    return args

def keywordsfun(**args):
    return args

def mix1(*argp, **argv):
    print(argp)
    print(argv)

# keyword arguments must follow the positional arguments
#def mix2(**argv, *argp):
#    print(argp)
#    print(argv)


first = posfun("Sudhir", "Surendra", "Bhoga")
second = keywordsfun(firstname='Sudhir', middlename="Surendra", lastname="Bhoga")
#mix1(firstname='Sudhir', middlename="Surendra", lastname="Bhoga", "Sudhir", "Surendra", "Bhoga")
mix1("Sudhir", "Surendra", "Bhoga", firstname='Sudhir', middlename="Surendra", lastname="Bhoga")

print(first)
print(second)

