#!/usr/bin/env python3

import os

workdir = os.getcwd()
# inputfile = "example_15.dat"
inputfile = "input_15.dat"


### first part ###

def hash_algorithm(string: str) -> int:
    """ Perform the hash algorithm as described on a given input sequence of characters. """
    
    hashnum = 0
    for char in string:
        hashnum += ord(char)
        hashnum *= 17
        hashnum = hashnum % 256

    return hashnum


with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()

sequences = []
for line in data:
    for seq in line.split(','):
        sequences.append(seq)

hashlist = [hash_algorithm(seq) for seq in sequences]

print(f'The sum of all results is: {sum(hashlist)}')


### second part ###

boxes = {i: {'labels': [], 'lengths': []} for i in range(256)}

for seq in sequences:

    if '-' in seq:
        label = seq.split('-')[0]
        box = hash_algorithm(label)
        if label in boxes[box]['labels']:
            index = boxes[box]['labels'].index(label)
            boxes[box]['labels'].remove(label)
            del(boxes[box]['lengths'][index])

    elif '=' in seq:
        label = seq.split('=')[0]
        length = int(seq.split('=')[1])
        box = hash_algorithm(label)
        if label in boxes[box]['labels']:
            index = boxes[box]['labels'].index(label)
            boxes[box]['lengths'][index] = length
        else:
            boxes[box]['labels'].append(label)
            boxes[box]['lengths'].append(length)
        
    else:
        print(f"ERROR: Sequence {seq} does not contain - or =. Erroneous input!")

power = 0
for box, content in boxes.items():
    for i in range(len(content['labels'])):
        power += (box+1) * (i+1) * content['lengths'][i]

print(f'The focusing power is: {power}')

