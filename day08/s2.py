import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
#from aocd import submit
#from dateutil.parser import parse


prob = []


with open('input', 'rt') as f:
    for line in f:
        sigs, outs = line.strip().split(' | ')
        sigs = sigs.split(' ')
        outs = outs.split(' ')
        prob.append((sigs, outs))


def solve(sigs, outs):
    lens = {
        'a': set(),
        'b': set(),
        'c': set(),
        'd': set(),
        'e': set(),
        'f': set(),
        'g': set(),
    }
    appears_in = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
    }
    known_lens = {
        2: 1,
        4: 4,
        3: 7,
        7: 8,
    }
    for s in sigs + outs:
        for ch in s:
            lens[ch].add(str(len(s)))
        if len(s) in known_lens:
            is_ = known_lens[len(s)]
            for ch in s:
                lens[ch].add(f'is_{is_}')
    for s in sigs:
        for ch in s:
            appears_in[ch] += 1
    for k in list(lens.keys()):
        lens[k].add(f'ap_in_{appears_in[k]}')
    for k in list(lens.keys()):
        lens[k] = tuple(sorted(lens[k]))

    # The `ans` map below maps onto the "canonical" 7-seg display with these labels:
    #    aaaa
    #   b    c
    #   b    c
    #    dddd
    #   e    f
    #   e    f
    #    gggg
    ans = {
        ('4', '5', '6', '7', 'ap_in_7', 'is_4', 'is_8')                           : 'd',
        ('2', '3', '4', '5', '6', '7', 'ap_in_9', 'is_1', 'is_4', 'is_7', 'is_8') : 'f',
        ('2', '3', '4', '5', '6', '7', 'ap_in_8', 'is_1', 'is_4', 'is_7', 'is_8') : 'c',
        ('4', '5', '6', '7', 'ap_in_6', 'is_4', 'is_8')                           : 'b',
        ('5', '6', '7', 'ap_in_7', 'is_8')                                        : 'g',
        ('5', '6', '7', 'ap_in_4', 'is_8')                                        : 'e',
        ('3', '5', '6', '7', 'ap_in_8', 'is_7', 'is_8')                           : 'a',
    }
    cannon_outs = [tuple(sorted([ans[lens[ch]] for ch in s])) for s in outs]

    decoder = {
        ('a', 'c', 'f'):                     7,
        ('c', 'f'):                          1,
        ('a', 'b', 'c', 'd', 'f', 'g'):      9,
        ('b', 'c', 'd', 'f'):                4,
        ('a', 'b', 'd', 'e', 'f', 'g'):      6,
        ('a', 'b', 'd', 'f', 'g'):           5,
        ('a', 'b', 'c', 'd', 'e', 'f', 'g'): 8,
        ('a', 'c', 'd', 'f', 'g'):           3,
        ('a', 'c', 'd', 'e', 'g'):           2,
        ('a', 'b', 'c', 'e', 'f', 'g'):      0,
    }
    value = int(''.join([str(decoder[co]) for co in cannon_outs]))
    return value


s = 0

for sigs, outs in prob:
    out = solve(sigs, outs)
    s += out
    #print('break')
    #break


print(s)

#submit(a)

