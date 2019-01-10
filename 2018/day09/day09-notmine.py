#!/usr/bin/python

#
# This great and lighning fast solution is heavily based on: https://www.michaelfogleman.com/aoc18/#9
# I was not awarare of deque
#

from collections import deque
import fileinput
import re
import argparse
import sys

parser = argparse.ArgumentParser(description='Advent of Code 2018 - Day 9 (part 2)')
parser.add_argument('--players', '-p', required=True, type=int)
parser.add_argument('--marbles', '-m', required=True, type=int)
parser.add_argument('--step', '-s', type=int, default=-1)
parser.add_argument('--magicmarble', '-g', type=int, default=23)
parser.add_argument('--magicstep', '-c', type=int, default=7)
args = parser.parse_args()


num_players = args.players
num_marbles = args.marbles
step = args.step
magic_marble = args.magicmarble
magic_step = args.magicstep

#num_players, num_marbles = map(int, re.findall(r'\d+', next(fileinput.input())))

def solve(num_players, num_marbles, step, magic_marble, magic_step):
    # initialize a double-ended queue with zero
    d = deque([0])
    # track score for each player
    scores = [0] * num_players
    for m in range(1, num_marbles + 1):
        if m % magic_marble == 0:
            d.rotate(magic_step)
            scores[m % num_players] += m + d.pop()
            d.rotate(step)
        else:
            d.rotate(step)
            d.append(m)
    return max(scores)

print solve(num_players, num_marbles, step, magic_marble, magic_step)


#from collections import defa
#d = deque([0])
#print d
#d.rotate(-1)
#d.append(1)
#print d
#d.rotate(-1)
#d.append(2)
#print d
#d.rotate(-1)
#d.append(3)
#print d

#print(solve(num_players, num_marbles))
#print(solve(num_players, num_marbles * 100))