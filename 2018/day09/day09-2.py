#!/usr/bin/python

import argparse
import sys
from collections import defaultdict

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None

class SingleLinkedList:

    def __init__(self, first_value=None):
        if first_value is not None:
            self.first_node = Node(first_value)
            self.length = 1
        else:
            self.first_node = None
            self.length = 0

    def get_node(self, index):
        current_node = self.first_node
        current_index = 0
        while current_node is not None and current_index < index:
            current_node = current_node.next_node
            current_index += 1
            
        if current_node is not None and current_index == index:
            return current_node
        else:
            raise ValueError("Index (%d) out of bounds" % (index))
    
    #def len(self):
    #    length = 0
    #    current_node = self.first_node
    #    while current_node is not None:
    #        current_node = current_node.next_node
    #        length += 1
    #    return length

    def get(self, index):
        return self.get_node(index).value

    def add(self, value):
        new_node = Node(value)
        new_node.next_node = self.first_node
        self.first_node = new_node
        self.length += 1
    
    def remove(self, index):
        removed_node = None
        if index == 0:
            removed_node = self.first_node
            self.first_node = removed_node.next_node
        else:
            previous_node = self.get_node(index - 1)
            removed_node = previous_node.next_node
            previous_node.next_node = removed_node.next_node

        self.length -= 1
        return removed_node.value
    
    def insert(self, index, value):
        if index < 0:
            raise ValueError("Please specify an index >= 0")

        if index == 0:
            self.add(value)
        else:
            current_node = self.get_node(index - 1)
            new_node = Node(value)
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node
            self.length += 1


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

def solve(number_of_players, number_of_marbles, step, magic_marble, magic_step):
    points = [0] * number_of_players
    marbles = SingleLinkedList(0)
    index_of_last_marble = 0
    for current_marble in range(1, number_of_marbles + 1):
        player = current_marble % number_of_players
        print "Marble: %d, Player: %d" % (current_marble, player)
        if current_marble % magic_marble == 0:
            length = marbles.length
            index_of_removed_marble = (length + (index_of_last_marble + magic_step)) % length
            removed_marble = marbles.remove(index_of_removed_marble)
            #marbles.remove(removed_marble)
            #print "Player %d keeping %d; removing %d (index: %d)" % (player, i, removedMarble, removedMarbleIndex)
            index_of_last_marble = index_of_removed_marble

            points[player] += current_marble + removed_marble
        else:
            index_of_current_marble = (index_of_last_marble + step - 1) % marbles.length + 1
            marbles.insert(index_of_current_marble, current_marble)
            index_of_last_marble = index_of_current_marble

    return max(points)

def print_list(linked_list):
    print "list:"
    current_node = linked_list.first_node
    while current_node:
        print current_node.value
        current_node = current_node.next_node

def test_list():
    linked_list = SingleLinkedList()
    linked_list.add(1)
    linked_list.add(2)
    print_list(linked_list)

    linked_list.insert(1, 3)
    print_list(linked_list)

    print "node at 3: %d" % linked_list.get_node(0).value

    print "removed %d" % linked_list.remove(-1)
    print_list(linked_list)

print solve(number_of_players, number_of_marbles, step, magic_marble, magic_step)