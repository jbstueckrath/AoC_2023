#!/usr/bin/env python3

import os

workdir = os.getcwd()
# inputfile = "example_04.dat"
inputfile = "input_04.dat"


### first part ###

with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()

points = 0
for line in data:
    wins = line.split('|')[0].split()[2:]
    mine = line.split('|')[1].split()
    n_wins = sum([1 if n in wins else 0 for n in mine])
    points += int(2 ** (n_wins-1))

print(f'The total worth of the cards is {points} points.')


### second part ###

instances = [0]*len(data)
for i, line in enumerate(data):
    instances[i] += 1
    n_wins = sum([1 if n in line.split('|')[0].split()[2:] else 0 for n in line.split('|')[1].split()])
    for n in range(n_wins): instances[i+n+1] += instances[i]

print(f'The total number of scratchcards is: {sum(instances)}')

