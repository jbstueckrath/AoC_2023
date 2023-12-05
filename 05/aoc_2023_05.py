#!/usr/bin/env python3

import os
import time

workdir = os.getcwd()
#inputfile = "example_05.dat"
inputfile = "input_05.dat"

timer_start = time.time()


### first part ###

def get_destination(inp_lines: list, trial: int) -> int:
    """ From a set of input lines [[destination, source, length], ...], return the destination for a trial source. """

    for line in inp_lines:
        if line[1] <= trial < line[1]+line[2]:
            return line[0] + trial - line[1]
    
    return trial


with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()

seeds = [int(i) for i in data[0].split()[1:]]
almanac = []
read = False
for index, line in enumerate(data):
    if 'map:' in line.split():
        read = True
        current_lines = []
        continue
    if read:
        current_lines.append([int(i) for i in line.split()])
        # Is there a better way of dealing with the end of the list?
        if index == len(data)-1:
            almanac.append(current_lines)
        elif not data[index+1]:
            almanac.append(current_lines)
            read = False

locations = []
for s in seeds:
    l = s
    for almanac_map in almanac:
        l = get_destination(almanac_map, l)
    locations.append(l)

print(f'The lowest location number that corresponds to an initial seed is: {min(locations)}')


### second part ###

"""
ATTENTION: This is a brute force solution and may take a lot of time.
With the input, it needs to try >2 billion trials which took >4h.
But hey, it worked in the end.
"""

n_seeds = sum([seeds[i] for i in range(len(seeds)) if (i+1) % 2 == 0])
lowest_location = max(locations)
counter = 0
for i in range(len(seeds)//2):
    for j in range(seeds[2*i+1]):
        l = seeds[2*i]+j
        for almanac_map in almanac:
            l = get_destination(almanac_map, l)
        if l < lowest_location: lowest_location = l
        counter += 1
        if counter % 1000000 == 0: print(f'Progress part 2: {counter/1000000:6.1f} M / {n_seeds/1000000:6.1f} M trials checked')

print(f'The lowest location number that corresponds to a new initial seed is: {lowest_location}')

timer_end = time.time()
print(f'The whole run took {timer_end-timer_start} seconds.')

