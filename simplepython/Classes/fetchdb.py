#!/usr/bin/env python

import shelve

db = shelve.open('persondb')

print("Number of Records : " + str(len(db)))
print(list(db.keys()))

for key in db:
    print (key, '=>', db[key].Address)

for key in db:
    print(key, '=>', db[key])
