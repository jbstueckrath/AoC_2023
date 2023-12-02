#!/usr/bin/env python3

import os
import math

workdir = os.getcwd()
# inputfile = "example_02.dat"
inputfile = "input_02.dat"


### first part ###

max_cubes = {'red': 12, 'green': 13, 'blue': 14}

with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()

max_draws = {}
for line in data:
    game_id = int(line.split()[1].replace(':', ''))
    draws = sum([d.split(',') for d in ''.join(line.split()[2:]).split(';')], [])
    num_draws = {'red': [], 'green': [], 'blue': []}
    for draw in draws:
        for color in max_cubes.keys():
            num_draws[color].append(int(draw[:-len(color)]) if color in draw else 0)
    max_draws[game_id] = {color: max(num_draws[color]) for color in max_cubes.keys()}

id_sum = 0
for id, game_max in max_draws.items():
    possible = True
    for color in max_cubes.keys():
        if game_max[color] > max_cubes[color]: possible = False
    if possible: id_sum += id

print(f'The sum of the IDs of all possible games is: {id_sum}')


### second part ###

power_sum = 0
for game_max in max_draws.values():
    power_sum += math.prod([game_max[color] for color in max_cubes.keys()])

print(f'The sum of power of all games is: {power_sum}')

