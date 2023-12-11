#!/usr/bin/env python3

import os
import math

workdir = os.getcwd()
# inputfile = "example_08_1.dat"
# inputfile = "example_08_2.dat"
# inputfile = "example_08_3.dat"
inputfile = "input_08.dat"


### first part ###

def get_steps(start, end):
    """ Return the number of steps necessary to reach an end point from the start. """

    current = start
    step = 0
    while current != end:
        current = network[current][instruction[step%len(instruction)]]
        step += 1
    
    return step


with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()

instruction = data[0]
network = {l.split()[0]: {'L': l.split()[2].replace('(', '').replace(',', ''), 'R': l.split()[3].replace(')', '')} for l in data[2:]}

start = 'AAA'
end = 'ZZZ'

print(f'The number of required steps to reach ZZZ is: {get_steps(start, end)}')


### second part ###

def get_steps_multi(starts):
    """ Return the number of steps for multiple start points until the label ends with Z. """

    steps = []
    for start in starts:
        current = start
        step = 0
        while current[-1] != 'Z':
            current = network[current][instruction[step%len(instruction)]]
            step += 1
        steps.append(step)
    
    return steps


starts = [k for k in network.keys() if k[-1] == 'A']
steps = get_steps_multi(starts)

# The answer is the least common multiple (LCM) of all step numbers, which exists as bulit-in math function
print(f'The number of required steps for all nodes to end with Z is: {math.lcm(*steps)}')

