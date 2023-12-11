#!/usr/bin/env python3

import os

workdir = os.getcwd()
# inputfile = "example_11.dat"
inputfile = "input_11.dat"


### first part ###

def get_dist_1d(a: int, b: int, empty: list[int]) -> int:
    """
    Return the distance of two points a and b within a row or column,
    taking into account the empty spaces and their expansion.
    """

    if a < b:
        start = a
        end = b
    elif a > b:
        start = b
        end = a
    else:
        return 0

    additional_space = 0
    for e in empty:
        if start < e < end: additional_space += expansion_add
    
    return end - start + additional_space


def get_dist_2d(gal_a: tuple[int, int], gal_b: tuple[int, int]) -> int:
    """ Get the distance (= shortest path) between two galaxies. """

    dist_x = get_dist_1d(gal_a[0], gal_b[0], empty_rows)
    dist_y = get_dist_1d(gal_a[1], gal_b[1], empty_cols)

    return dist_x + dist_y


def get_dist_sum(galaxies: list[tuple[int, int]]) -> int:
    """ Retrun the sum of distances between all galaxies. """

    sum_dist = 0
    for a, gal_a in enumerate(galaxies):
        for b in range(len(galaxies)-a-1):
            sum_dist += get_dist_2d(gal_a, galaxies[b+a+1])
    
    return sum_dist


with open(os.path.join(workdir, inputfile)) as inp:
    image = inp.read().splitlines()

expansion_add = 1

galaxies = []
empty_rows = []
for i, row in enumerate(image):
    if '#' in row:
        for j, col in enumerate(row):
            if col == '#': galaxies.append((i, j))
    else: empty_rows.append(i)

empty_cols = []
for j in range(len(image[0])):
    if not '#' in [image[i][j] for i in range(len(image))]:
        empty_cols.append(j)

print(f'The sum of all shortest path lengths is: {get_dist_sum(galaxies)}')


### second part ###

expansion_add = 999999

print(f'The sum of all shortest path lengths with the larger expansion is: {get_dist_sum(galaxies)}')

