#!/usr/bin/env python

personal = {'firstname':'Sudhir', 'middlename':'Surendra', 'surname':'Bhoga'}
print(type(personal))
print(len(personal))

print(personal)
print(personal['middlename'])

for k,v in personal.items():
    print(k, v)


vowels = ['a', 'e', 'i', 'o', 'u']

for k,v in enumerate(vowels):
    print(k, v)
