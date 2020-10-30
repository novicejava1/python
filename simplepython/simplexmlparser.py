#!/usr/bin/env python
from bs4 import BeautifulSoup

file = open("sample.xml", "r")
soup = BeautifulSoup(file, features='lxml')

#print(soup.prettify())

po=soup.find("px:id", typecode="PO")
print("po : " + po.get_text())

items=soup.find("px:id", typecode="Item Of Purchasing Doc")
print("items : " + items.get_text())

