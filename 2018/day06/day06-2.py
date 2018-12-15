#!/usr/bin/python

import re, operator
from operator import sub
from itertools import product

#file = open("test-input.txt")
file = open("input.txt")
lines = file.read().split("\n")

coordinates = dict()

# parse coordinates
for i, line in enumerate(lines):
    coordinateLine = line.split(", ")
    coordinates[i+1] = (int(coordinateLine[0]), int(coordinateLine[1]))

#max(map(coordinates.values()[0][1]

max_x = max(x[0] for x in coordinates.values()) #+ 1
max_y = max(y[1] for y in coordinates.values()) #+ 1

#print max_x, max_y

coordinate_space = [ [0 for y in range(0, max_y)] for x in range(0, max_x)]
coordinate_map = dict()

#for id, pos in coordinates.iteritems():
#    coordinate_space[pos[0]][pos[1]] = id

#a = (1,2)
#b = (1,1)
#print reduce(operator.and_, map(operator.eq, a, b))
#print coordinates.values()
#infinites = set()
sum_d_reg = 0
for x,y in product(range(0, max_x), range(0, max_y)):
    #print map(sub, [[1,1]], [[1,1]])
    distances = dict()

    sumD = 0
    for id, pos in coordinates.iteritems():
        d = sum(map(abs, map(sub, (x,y), pos)))
        sumD += d
        try:
            distances[d].append(id)
        except:
            distances[d] = [id]
    dmin = min(distances.keys())
    
    #if len(distances[dmin]) == 1:
    #    coordinate_space[x][y] = distances[dmin][0]
    #    
    #    try: 
    #        coordinate_map[distances[dmin][0]].append((x,y))
    #    except:
    #        coordinate_map[distances[dmin][0]] = [(x,y)]
    
    #    if x == 0 or y == 0 or x == max_x -1 or y == max_y -1:
    #        infinites.update(distances[dmin])
    
    #if sumD < 32:
    if sumD < 10000:
        coordinate_space[x][y] = 9
        sum_d_reg += 1


#finites = set(coordinates.keys()).difference(infinites)
print sum_d_reg

#for fin in finites:
#    print len(coordinate_map[fin])

#print max(len(coordinate_map[fin]) for fin in finites)

#for x in coordinate_space:
#    print " ".join(map(str, x))
#print coordinate_space

#absolute_value = sum(map(abs, map(sub, a, b)))
#print absolute_value