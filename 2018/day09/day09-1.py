#!/usr/bin/python

import argparse
import sys
from collections import defaultdict


parser = argparse.ArgumentParser(description='Advent of Code 2018 - Day 9 (part 1)')
parser.add_argument('--players', '-p', required=True, type=int)
parser.add_argument('--marbles', '-m', required=True, type=int)
parser.add_argument('--step', '-s', type=int, default=2)
parser.add_argument('--magicmarble', '-g', type=int, default=23)
parser.add_argument('--magicstep', '-c', type=int, default=-7)
args = parser.parse_args()

number_of_players = args.players
number_of_marbles = args.marbles

step = args.step
magic_marble = args.magicmarble
magic_step = args.magicstep

points = [0] * number_of_players
marbles = [0]
index_of_last_marble = 0
for current_marble in range(1, number_of_marbles + 1):
    player = current_marble % number_of_players
    #print "Marble: %d, Player: %d" % (current_marble, player)
    if current_marble % magic_marble == 0:
        index_of_removed_marble = (len(marbles) + (index_of_last_marble + magic_step)) % len(marbles)
        removed_marble = marbles[index_of_removed_marble]
        marbles.remove(removed_marble)
        #print "Player %d keeping %d; removing %d (index: %d)" % (player, i, removedMarble, removedMarbleIndex)
        index_of_last_marble = index_of_removed_marble

        points[player] += current_marble + removed_marble
    else:
        index_of_current_marble = (index_of_last_marble + step - 1) % len(marbles) + 1
        marbles.insert(index_of_current_marble, current_marble)
        index_of_last_marble = index_of_current_marble

print max(points)
