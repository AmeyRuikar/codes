#! /usr/bin/python

import re
import sys

f = open('text.rtf')

exp = re.compile('if', re.I)


count = sys.argv[1];
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
