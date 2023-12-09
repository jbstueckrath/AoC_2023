#!/usr/bin/env python3

import os

workdir = os.getcwd()
# inputfile = "example_09.dat"
inputfile = "input_09.dat"


### first part ###

def get_diff(sequence: list[int]) -> list[int]:
    """ From a given sequence, retrun a list of differences. """

    return [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]

def get_next(sequence: list[int]) -> list[int]:
    """ From a given sequence, return the next value as described in the puzzle. """

    diff = sequence.copy()
    lastval = []
    while any(diff):
        diff = get_diff(diff)
        lastval.append(diff[-1])
    nextval = sequence[-1] + sum(lastval)

    return nextval


with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()

next_values = [get_next([int(i) for i in line.split()]) for line in data]

print(f'The sum of all extrapolated next values is: {sum(next_values)}')


### second part ###

def get_previous(sequence: list[int]) -> list[int]:
    """ From a given sequence, return the previous value as described in the puzzle. """

    diff = sequence.copy()
    firstval = []
    while any(diff):
        diff = get_diff(diff)
        firstval.append(diff[0])
    tmp = 0
    for i in reversed(firstval): tmp = i - tmp
    previousval = sequence[0] - tmp

    return previousval

previous_values = [get_previous([int(i) for i in line.split()]) for line in data]

print(f'The sum of all extrapolated previous values is: {sum(previous_values)}')

