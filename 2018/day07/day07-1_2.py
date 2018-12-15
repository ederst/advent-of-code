#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='Advent of Code 2018 - Day 7 (part 1 & 2)')
parser.add_argument('--input', '-i', required=True, type=file)
parser.add_argument('--timedilution', '-t', type=int, default=0)
parser.add_argument('--workers', '-w', type=int, default=1)

args = parser.parse_args()

max_worker = args.workers
timeDilution = args.timedilution
file = args.input

#file = open("test-input_2.txt")
#file = open("input.txt")
lines = file.read().split("\n")

nodes = dict()

for line in lines:
    nodeLine = line.split(" ")
    parentId = nodeLine[1]
    childId = nodeLine[7]

    # Step C must be finished before step A can begin.
    try:
        data = nodes[childId]
    except:
        nodes[childId] = { "dependsOn" : set(parentId), "children" : set(), "dist" : -1 }
    nodes[childId]["dependsOn"].update(parentId)

    try:
        data = nodes[parentId]
    except:
        nodes[parentId] = { "dependsOn" : set(), "children" : set(childId), "dist" : -1 }
    nodes[parentId]["children"].update(childId)

toProcess = []
for id, data in nodes.iteritems():
    if not data["dependsOn"]:
        toProcess.append(id)

def canExecute(id):
    dependsOn = nodes[id]["dependsOn"]
    if any(dep not in executed or dep in toProcess or dep in in_execution for dep in dependsOn):
        return None
    return id

def calcTime(id):
    return id[1] + ord(id[0]) - 64 + timeDilution

executed = []
in_execution = []
currentTick = 0
while toProcess or in_execution:
    toProcess.sort(reverse=True)
    print "to proc: %s" % toProcess
    i = 0
    while toProcess and len(in_execution) < max_worker:
        in_execution.append((toProcess.pop(), currentTick))
        i += 1
    print "in exec: %s" % in_execution
    
    # advance in time...
    #currentTick = reduce(min, [calcTime(id) for id in in_execution])
    currentTick = reduce(min, map(calcTime, in_execution))
    
    print "current tick: %d" % currentTick
    for id in in_execution:   
        if calcTime(id) <= currentTick:
            in_execution.remove(id)
            executed.append(id[0])
            toProcess.extend(list(filter(lambda x: canExecute(x) is not None, nodes[id[0]]["children"])))


print "".join(executed)