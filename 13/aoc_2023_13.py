#!/usr/bin/env python3

"""
ATTENTION: This code is quite complex and difficult to read.
But it works.
"""

import os

workdir = os.getcwd()
# inputfile = "example_13.dat"
inputfile = "input_13.dat"


### first part ###

def get_reflection_lines(pattern: list[list]) -> tuple[int, int]:
    """ Searches for the reflection line in a pattern and returns the number of rows above or colums left the line. """

    rows_above = 0

    # search for two neighboring identical rows
    for i_row in range(len(pattern)-1):
        if pattern[i_row] == pattern[i_row+1]:
            found_reflection = True

            # go through all rows away from the mirror until the end of the pattern
            for j_row in range(i_row):
                try:
                    if pattern[i_row-j_row-1] != pattern[i_row+j_row+2]:
                        found_reflection = False
                except IndexError:
                    break
            
            # reflection line is found if no differences were found
            if found_reflection:
                rows_above = i_row + 1
                break

    # do the same analogously for the columns
    colums_left = 0
    for i_col in range(len(pattern[0])-1):
        if all([row[i_col] == row[i_col+1] for row in pattern]):
            found_reflection = True

            for j_col in range(i_col):
                try:
                    if not all([row[i_col-j_col-1] == row[i_col+j_col+2] for row in pattern]):
                        found_reflection = False
                except IndexError:
                    break

            if found_reflection:
                colums_left = i_col + 1
                break

    return colums_left, rows_above


with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()

patterns = []
pattern = []
for i, line in enumerate(data):
    if line != '':
        pattern.append(line)
    if line == '' or i == len(data)-1:
        patterns.append(pattern)
        pattern = []

sum_notes = 0
for pattern in patterns:
    left, above = get_reflection_lines(pattern)
    sum_notes += left + 100*above

print(f'The summarized number of notes is: {sum_notes}')


### second part ###

def different_by_one(list_a: list, list_b: list) -> bool:
    """ Check if two lists (or strings) differ by exactly one element (character). """

    differences = ['#' for i in range(len(list_a)) if list_a[i] != list_b[i]]
    return len(differences) == 1


def get_reflection_lines_new(pattern: list[list]) -> tuple[int, int]:
    """ Searches for the smudge and returns the number of rows above or colums left the new reflection line. """

    rows_above = 0

    # search for two lines that differ by only one element
    for i_row in range(len(pattern)-1):
        for j_row in range((len(pattern)-i_row) // 2):
            next_row = i_row+2*j_row+1
            if different_by_one(pattern[i_row], pattern[next_row]):
                above_row = i_row  + (next_row-i_row+1) // 2

                # create a list[bool] to check for idential rows starting from the first line next to the mirror
                checklist = []
                for k in range(above_row):
                    ind_prev = above_row-1-k
                    ind_next = above_row+k
                    if ind_prev < 0 or ind_next > len(pattern)-1:
                        break
                    if ind_prev == i_row:
                        checklist.append(True)
                        continue
                    checklist.append(pattern[ind_prev] == pattern[ind_next])
                
                # the new reflection line is found only if all other important lines are identical
                if all(checklist):
                    rows_above = above_row
    
    # do the same analogously for the columns
    colums_left = 0
    for i_col in range(len(pattern[0])-1):
        for j_col in range((len(pattern[0])-i_col) // 2):
            next_col = i_col+2*j_col+1
            if different_by_one([p[i_col] for p in pattern], [p[next_col] for p in pattern]):
                left_col = i_col + (next_col-i_col+1) // 2

                checklist = []
                for k in range(left_col):
                    ind_prev = left_col-1-k
                    ind_next = left_col+k
                    if ind_prev < 0 or ind_next > len(pattern[0])-1:
                        break
                    if ind_prev == i_col:
                        checklist.append(True)
                        continue
                    checklist.append([p[ind_prev] for p in pattern] == [p[ind_next] for p in pattern])

                if all(checklist):
                    colums_left = left_col

    return colums_left, rows_above


sum_notes_new = 0
for pattern in patterns:
    left, above = get_reflection_lines_new(pattern)
    sum_notes_new += left + 100*above

print(f'The new summarized number of notes is: {sum_notes_new}')

