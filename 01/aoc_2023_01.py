#!/usr/bin/env python3

import os

workdir = os.getcwd()
#inputfile = "example_01_1.dat"
#inputfile = "example_01_2.dat"
inputfile = "input_01.dat"


### first part ###

def getval(line: str) -> int:
    """ Retrun the calibration value of an input line. """

    first = None
    last = None
    for c in line:
        if c.isdigit():
            first = c
            break
    for c in reversed(line):
        if c.isdigit():
            last = c
            break
    if first is None or last is None:
        print(f'ATTENTION: Did not find any number in string {line} ! Adding 0...')
        return 0

    return int(first+last)


with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()

sum_values = 0
for line in data: sum_values += getval(line)

print(f'The sum of the calibration values is: {sum_values}')


### second part ###

digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def getdigit(line: str, index: int) -> str:
    """ Return a string digit if a corresponding word is found in the line. """

    digit = None
    for n in [3, 4, 5]:
        if line[index:index+n] in digits.keys():
            digit = digits[line[index:index+n]]
    
    return digit


def getval_correct(line: str) -> int:
    """ Retrun the correct calibration value of an input line. """

    first = None
    last = None
    for i, c in enumerate(line):
        digit = getdigit(line, i)
        if c.isdigit():
            first = c
            break
        if digit is not None:
            first = digit
            break
    for i, c in enumerate(reversed(line)):
        digit = getdigit(line, len(line)-i-1)
        if c.isdigit():
            last = c
            break
        if digit is not None:
            last = digit
            break

    if first is None or last is None:
        print(f'ATTENTION: Did not find any number in string {line} ! Adding 0...')
        return 0

    return int(first+last)

sum_values_correct = 0
for line in data: sum_values_correct += getval_correct(line)

print(f'The correct sum of the calibration values is: {sum_values_correct}')

