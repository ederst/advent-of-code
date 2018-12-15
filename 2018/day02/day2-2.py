#!/usr/bin/python
from itertools import product

file = open("input.txt")
#file = open("test-input_2.txt")

lines = file.read().split("\n")

for line, otherline in product(lines,lines):
    zipline = zip(line, otherline)
        
    count = 0
    index = -1
    for i, val in enumerate(zipline):
        if val[0] != val[1]:
            count += 1
            if count > 1:
                break
            else:
                matchIndex = i
    
    if count == 1:
        print "%s vs %s -> %s" % (line, otherline, line[:index] + line[index+1:])
        exit()
