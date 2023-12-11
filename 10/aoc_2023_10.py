#!/usr/bin/env python3

import os

workdir = os.getcwd()
# inputfile = "example_10_1.dat"
# inputfile = "example_10_2.dat"
inputfile = "input_10.dat"


### first part ###

def get_S(pipe_map: list[str]) -> tuple[int, int]:
    """ Search for S in the map and return its coordinates. """

    for i, row in enumerate(pipe_map):
        if 'S' in row:
            for j, col in enumerate(row):
                if col == 'S': return (i, j)


def get_start(pipe_map: list[str]) -> tuple[tuple[int, int], tuple[int, int], str]:
    """
    From S in the map, return:
        the coordinates of s,
        the coordinates of one of the two possible next pipes,
        and the resulting type, the tile behind S must have.
    """

    coord_s = get_S(pipe_map)
    coord_next = (None, None)
    env_s = {'a': False, 'b': False, 'l': False, 'r': False}
    type_s = None

    if coord_s[0] > 0:
        above = pipe_map[coord_s[0]-1][coord_s[1]]
        if above in ['|', '7', 'F']:
            coord_next = (coord_s[0]-1, coord_s[1])
            env_s['a'] =  True
    if coord_s[0] < len(pipe_map)-1:
        below = pipe_map[coord_s[0]+1][coord_s[1]]
        if below in ['|', 'L', 'J']:
            coord_next = (coord_s[0]+1, coord_s[1])
            env_s['b'] =  True
    if coord_s[1] > 0:
        left = pipe_map[coord_s[0]][coord_s[1]-1]
        if left in ['-', 'L', 'F']:
            coord_next = (coord_s[0], coord_s[1]-1)
            env_s['l'] =  True
    if coord_s[1] < len(pipe_map[0])-1:
        right = pipe_map[coord_s[0]][coord_s[1]+1]
        if right in ['-', 'J', '7']:
            coord_next = (coord_s[0], coord_s[1]+1)
            env_s['r'] =  True
    
    if env_s['a'] and env_s['b'] : type_s = '|'
    elif env_s['a'] and env_s['l'] : type_s = 'J'
    elif env_s['a'] and env_s['r'] : type_s = 'L'
    elif env_s['l'] and env_s['r'] : type_s = '-'
    elif env_s['l'] and env_s['b'] : type_s = '7'
    elif env_s['b'] and env_s['r'] : type_s = 'F'
    
    return coord_s, coord_next, type_s


def get_next_coord(coord_prev: tuple[int, int], coord_curr: tuple[int, int], type_curr: str) -> tuple[int, int]:
    """
    From the coordinates of the previous and the current pipe and the current type,
    return the coordinates of the resulting next pile in the loop.
    """

    if type_curr == '|':
        if coord_prev[0] < coord_curr[0]: return (coord_curr[0]+1, coord_curr[1])
        else: return (coord_curr[0]-1, coord_curr[1])
    elif type_curr == '-':
        if coord_prev[1] < coord_curr[1]: return (coord_curr[0], coord_curr[1]+1)
        else: return (coord_curr[0], coord_curr[1]-1)
    elif type_curr == 'L':
        if coord_prev[0] == coord_curr[0]: return (coord_curr[0]-1, coord_curr[1])
        else: return (coord_curr[0], coord_curr[1]+1)
    elif type_curr == 'J':
        if coord_prev[0] == coord_curr[0]: return (coord_curr[0]-1, coord_curr[1])
        else: return (coord_curr[0], coord_curr[1]-1)
    elif type_curr == '7':
        if coord_prev[0] == coord_curr[0]: return (coord_curr[0]+1, coord_curr[1])
        else: return (coord_curr[0], coord_curr[1]-1)
    elif type_curr == 'F':
        if coord_prev[0] == coord_curr[0]: return (coord_curr[0]+1, coord_curr[1])
        else: return (coord_curr[0], coord_curr[1]+1)


with open(os.path.join(workdir, inputfile)) as inp:
    full_map = inp.read().splitlines()

previous, current, _ = get_start(full_map)
loop_pipes = [current]
while not full_map[current[0]][current[1]] == 'S':
    tmp = current
    current = get_next_coord(previous, current, full_map[current[0]][current[1]])
    previous = tmp
    loop_pipes.append(current)

print(f'The number of steps to the farthest point is: {len(loop_pipes)//2}')


### second part ###

s_coord, _, s_type = get_start(full_map)
full_map[s_coord[0]] = full_map[s_coord[0]].replace('S', s_type)

enclosed = 0
inside = False
for i, row in enumerate(full_map):
    for j, col in enumerate(row):
        if (i, j) in loop_pipes:
            if full_map[i][j] in ['|', 'L', 'F']:
                inside = not inside
                curr_edge = full_map[i][j]
            elif (full_map[i][j] == 'J' and curr_edge == 'L') or (full_map[i][j] == '7' and curr_edge == 'F'):
                inside = not inside
        else:
            if inside: enclosed += 1

print(f'The number of tiles encloded by the loop is: {enclosed}')

