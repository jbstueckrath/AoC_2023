#!/usr/bin/env python3

import os

workdir = os.getcwd()
# inputfile = "example_03.dat"
inputfile = "input_03.dat"


### first part ###

def issymbol(character):
    """ Check if the investigated character is a symbol. """

    return not (character.isdigit() or character == '.')

def get_blankline(line):
    """ Return a line with blank spaces istead of . or symbols. """

    return ''.join([c if c.isdigit() else ' ' for c in line])

def get_surroundnigs(i_row, row, i_col):
    """ Get all surrounding characters of the one in line, with index (= row) and i (= column). """

    surroundings = []
    if i_col > 0:
        surroundings.append((row[i_col-1], i_row, i_col-1))
        if i_row > 0: surroundings.append((data[i_row-1][i_col-1], i_row-1, i_col-1))
        if i_row < len(data)-1: surroundings.append((data[i_row+1][i_col-1], i_row+1, i_col-1))
    if i < len(row)-1:
        surroundings.append((row[i_col+1], i_row, i_col+1))
        if i_row > 0: surroundings.append((data[i_row-1][i_col+1], i_row-1, i_col+1))
        if i_row < len(data)-1: surroundings.append((data[i_row+1][i_col+1], i_row+1, i_col+1))
    if i_row > 0: surroundings.append((data[i_row-1][i_col], i_row-1, i_col))
    if i_row < len(data)-1: surroundings.append((data[i_row+1][i_col], i_row+1, i_col))

    return surroundings


with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()

lineentries = []
next_to_ast = {}
gears = []
for i_line, line in enumerate(data):
    entrycount = -1
    entries = []
    read = False
    ispart = False
    isast = False
    included = False
    for i, c in enumerate(line):
        if c.isdigit():
            read = True
            for around in get_surroundnigs(i_line, line, i):
                if issymbol(around[0]): ispart = True
                if around[0] == '*':
                    isast = True
                    ast = (around[1], around[2])
                    if ','.join(str(xy) for xy in ast) in next_to_ast.keys(): included = True
        if (not c.isdigit() or i == len(line)-1) and read == True:
            entrycount += 1
            read = False
            if ispart:
                entries.append(entrycount)
                ispart = False
            if isast:
                if included:
                    part_1 = tuple([int(i) for i in next_to_ast[','.join(str(xy) for xy in ast)].split(',')])
                    part_2 = (i_line, entrycount)
                    gears.append((part_1, part_2))
                    included = False
                else:
                    next_to_ast[','.join(str(xy) for xy in ast)] = ','.join(str(xy) for xy in [i_line, entrycount])
                    isast = False
    lineentries.append(entries)

blankdata = []
sum_part_numbers = 0
sum_gear_ratio = 0
for i_line, line in enumerate(data): blankdata.append(get_blankline(line).split())
for i_line, entries in enumerate(lineentries):
    for e in entries:
        sum_part_numbers += int(blankdata[i_line][e])
for pair in gears: sum_gear_ratio += int(blankdata[pair[0][0]][pair[0][1]]) * int(blankdata[pair[1][0]][pair[1][1]])

print(f'The sum of all part numbers is: {sum_part_numbers}')


### second part ###

"""
This code was written to work independently from part 1.
However, it was later incorporated in the loop of part 1 and is now deprecated.
"""

# next_to_ast = {}
# gears = []
# for i_line, line in enumerate(data):
#     entrycount = -1
#     read = False
#     isast = False
#     included = False
#     for i, c in enumerate(line):
#         if c.isdigit():
#             read = True
#             for around in get_surroundnigs(i_line, line, i):
#                 if around[0] == '*':
#                     isast = True
#                     ast = (around[1], around[2])
#                     if ','.join(str(xy) for xy in ast) in next_to_ast.keys(): included = True
#         if (not c.isdigit() or i == len(line)-1) and read == True:
#             entrycount += 1
#             read = False
#             if isast:
#                 if included:
#                     part_1 = tuple([int(i) for i in next_to_ast[','.join(str(xy) for xy in ast)].split(',')])
#                     part_2 = (i_line, entrycount)
#                     gears.append((part_1, part_2))
#                     included = False
#                 else:
#                     next_to_ast[','.join(str(xy) for xy in ast)] = ','.join(str(xy) for xy in [i_line, entrycount])
#                     isast = False

# blankdata = []
# sum_gear_ratio = 0
# for i_line, line in enumerate(data): blankdata.append(get_blankline(line).split())
# for pair in gears: sum_gear_ratio += int(blankdata[pair[0][0]][pair[0][1]]) * int(blankdata[pair[1][0]][pair[1][1]])

print(f'The sum of all gear ratios is: {sum_gear_ratio}')

