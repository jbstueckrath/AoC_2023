#!/usr/bin/env python3

import os
from collections.abc import Callable

workdir = os.getcwd()
# inputfile = "example_07.dat"
inputfile = "input_07.dat"


### first part ###

card_values = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def get_card_value(label: str) -> int:
    """ Returns the numerical value of a card label. """

    if label.isdigit(): return int(label)
    else: return card_values[label]

def get_score(cards: list[int]) -> int:
    """ Returns the type of the hand as a score ranked from 1-7. """

    occurances = [cards.count(i+2) for i in range(13)]
    if 5 in occurances: return 7               # five of a kind
    elif 4 in occurances: return 6             # four of a kind
    elif 3 in occurances:
        if 2 in occurances: return 5           # full house
        else: return 4                         # three of a kind
    elif 2 in occurances:
        if occurances.count(2) > 1: return 3   # two pair
        else: return 2                         # one pair
    else: return 1                             # high card

def get_hands(lines: list[str], rules: Callable[[list[int]], int]) -> list[dict]:
    """ Retruns a list of all hands from the input file and a function specifying the rules. """

    hands = []
    for line in lines:
        cards = [get_card_value(c) for c in line.split()[0]]
        hands.append({
            'cards': cards,
            'score': rules(cards),
            'bid': int(line.split()[1])
        })
    
    return hands


with open(os.path.join(workdir, inputfile)) as inp:
    data = inp.read().splitlines()


hands = get_hands(data, get_score)
hands_sorted = sorted(hands, key=lambda k: (k['score'], k['cards']))
winnings = [(i+1) * h['bid'] for i, h in enumerate(hands_sorted)]

print(f'The total winnings of all hands are: {sum(winnings)}')


### second part ###

card_values['J'] = 1

def get_score_new(cards: list[int]) -> int:
    """ Returns the type of the hand with the new rules as a score ranked from 1-7. """

    occurances = sorted([cards.count(i+2) for i in range(13)], reverse=True)
    highest_kind = occurances[0] + cards.count(1)
    second_highest = occurances[1]

    if highest_kind == 5: return 7        # five of a kind
    elif highest_kind == 4: return 6      # four of a kind
    elif highest_kind == 3:
        if second_highest > 1: return 5   # full house
        else: return 4                    # three of a kind
    elif highest_kind == 2:
        if second_highest > 1: return 3   # two pair
        else: return 2                    # one pair
    else: return 1                        # high card

hands_sorted_new = sorted(get_hands(data, get_score_new), key=lambda k: (k['score'], k['cards']))
winnings_new = [(i+1) * h['bid'] for i, h in enumerate(hands_sorted_new)]

print(f'The total winnings of all hands with the new rules are: {sum(winnings_new)}')

