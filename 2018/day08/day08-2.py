#!/usr/bin/python

import argparse
import sys

#sys.setrecursionlimit(1000)
#print sys.getrecursionlimit()
#exit()

parser = argparse.ArgumentParser(description='Advent of Code 2018 - Day 8 (part 1)')
parser.add_argument('--input', '-i', required=True, type=file)
#parser.add_argument('--timedilution', '-t', type=int, default=0)
#parser.add_argument('--workers', '-w', type=int, default=1)
args = parser.parse_args()

file = args.input
lines = file.read().split("\n")

nodes = dict()

def getMetaData(startPos):
    node_nr = startPos
    endPos = startPos + 1
    
    nodeHeader = nodeLine[startPos:endPos + 1]
    
    #print "nodeHeader: %s (%d, %d)" % (nodeHeader, startPos, endPos)
    children_n = int(nodeHeader[0])
    metadata_n = int(nodeHeader[1])

    children = []
    metadata_all = []
    for i in range(0, children_n):
        child_nr = endPos + 1
        endPos, metadata = getMetaData(child_nr)
        children.append(int(child_nr))
        metadata_all.extend(metadata)

    startPos = endPos
    endPos = endPos + metadata_n
    metadata = nodeLine[startPos +1:endPos + 1]
    metadata_all.extend(metadata)
    #print metadata_all
    value = 0
    if (children_n == 0):
        value = reduce(lambda x,y: x+y, map(int, metadata))

    nodes[node_nr] = { "header" : nodeHeader, "metadata" : metadata, "value" : value, "children" : children }
    #print node_nr, nodes[node_nr]
    return endPos, metadata_all

def getValue(node_nr):
    node = nodes[node_nr]

    value = node["value"]
    if value == 0:
        children = node["children"]
        for i in node["metadata"]:
            i = int(i)
            if i <= len(children):
                value += getValue(children[i - 1])

    return value

for line in lines:
    nodeLine = line.split(" ")
    endPos, metadata = getMetaData(0)
    print "sum of metadata: %d" % reduce(lambda x,y: x+y, map(int, metadata))
    print "value of root node: %d" % getValue(0)

    
