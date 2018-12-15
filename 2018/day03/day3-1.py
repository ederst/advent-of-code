#!/usr/bin/python

from itertools import product

#file = open("test-input.txt")
file = open("input.txt")
lines = file.read().split("\n")

coordinates = dict()

for line in lines:
    splitLine = line.split(" ")
    
    point1 = splitLine[2].replace(":","").split(",")
    point2 = splitLine[3].split("x")

    x1 = int(point1[0])
    x2 = x1 + int(point2[0])

    y1 = int(point1[1])
    y2 = y1 + int(point2[1])

    for x, y in product(range(x1, x2), range(y1, y2)):
        key = "%d,%d" % (x,y)
#       imperformant as fuck
        print key
#        if key in coordinates.keys():
#            coordinates[key] += 1
#        else:
#            coordinates[key] = 0
        try:
            coordinates[key] += 1
        except:
            coordinates[key] = 0

sqInches = 0
for k,v in coordinates.iteritems():
    if v > 0:
        sqInches += 1
print sqInches