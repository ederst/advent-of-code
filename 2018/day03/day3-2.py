#!/usr/bin/python

from itertools import product

#file = open("test-input.txt")
file = open("input.txt")
lines = file.read().split("\n")

coordinates = dict()

allIds = set()
for line in lines:
    splitLine = line.split(" ")
    
    theId = splitLine[0]
    allIds.add(theId)

    point1 = splitLine[2].replace(":","").split(",")
    point2 = splitLine[3].split("x")

    x1 = int(point1[0])
    x2 = x1 + int(point2[0])

    y1 = int(point1[1])
    y2 = y1 + int(point2[1])
    
    for x, y in product(range(x1, x2), range(y1, y2)):
        key = "%d,%d" % (x,y)
        try:
            coordinates[key].append(theId)
        except:
            coordinates[key] = [theId]

sqInches = 0
overlappers = set()
for k,v in coordinates.iteritems():
    if len(v) > 1:
        sqInches += 1
        for o in v:
            overlappers.add(o)

print allIds.difference(overlappers)
print len(overlappers)
print sqInches