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

def getMetaData(startPos):
    endPos = startPos + 1
    
    nodeHeader = nodeLine[startPos:endPos + 1]
    
    #print "nodeHeader: %s (%d, %d)" % (nodeHeader, startPos, endPos)
    children_n = int(nodeHeader[0])
    metadata_n = int(nodeHeader[1])

    metadata_all = []
    for i in range(0, children_n):
        endPos, metadata = getMetaData(endPos + 1)
        metadata_all.extend(metadata)

    startPos = endPos
    endPos = endPos + metadata_n
    metadata_all.extend(nodeLine[startPos +1:endPos + 1])
    #print metadata_all

    return endPos, metadata_all

for line in lines:
    nodeLine = line.split(" ")
    #print nodeLine
    #print reduce(lambda x,y: x+y, getMetaData(0))
    endPos, metadata = getMetaData(0)
    #print endPos, metadata
    print "sum of metadata: %d" % reduce(lambda x,y: x+y, map(int, metadata))
    
