#! /usr/bin/python

import re

f = open('text.rtf')

exp = re.compile('if', re.I)

count = 10;
lineNumber = 0;

for line in f:
    lineNumber = lineNumber + 1
    searchObj = exp.search(line)

    if searchObj:
        print(lineNumber)
        print(" -> "+line)
        count = count-1

    if count == 0:
        break;
