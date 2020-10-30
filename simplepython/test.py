#!/usr/bin/env python

from bs4 import BeautifulSoup

infile = open("file1.txt", "r")
contents = infile.read()
#infile.close()
soup = BeautifulSoup(contents, 'lxml')
print(soup)
IDtags = soup.find_all('px:ID', typeCode=True)
print(IDtags)
with open("file2.txt", "w") as outfile:
    for tag in IDtags:
        outfile.write(tag['PO'] + ' : ' + tag.get_text() + '\n')
