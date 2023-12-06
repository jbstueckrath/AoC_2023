#!/usr/bin/env python3

import os
import math

workdir = os.getcwd()
# inputfile = "example_06.dat"
inputfile = "input_06.dat"


### first part ###

def get_distance(max_time: int, hold: int) -> int:
    """ Retrun the travelled distance in a race of a given maximum time and button-holding-time. """

    return (max_time - hold) * hold

def get_wins(race: dict) -> int:
    """ Return the number of possible ways to win in a given race. """
    
    losses = 0
    for i in range(race['time']+1):
        if get_distance(race['time'], i) <= race['record']: losses += 1
        else: break

    return race['time']+1 - 2*losses


with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()

races = [{'time': int(data[0].split()[1:][i]), 'record': int(data[1].split()[1:][i])} for i in range(len(data[0].split())-1)]
prod_wins = math.prod([get_wins(r) for r in races])

print(f'The product of all numbers of possible ways to win is: {prod_wins}')


### second part ###

correct_race = {key: int(''.join([str(r[key]) for r in races])) for key in races[0].keys()}
wins = get_wins(correct_race)

print(f'The number of possible ways to beat the record in the correct race is: {wins}')

