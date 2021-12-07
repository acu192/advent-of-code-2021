import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
#from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    s = [int(c) for c in f.read().strip().split(',')]

lineon = None
min_cost = 99999999999999999

cache = {}

def calc_cost(from_, to):
    diff = abs(from_ - to)
    if diff in cache:
        return cache[diff]
    cost = 0
    for _ in range(diff):
        cost += (_ + 1)
    cache[diff] = cost
    return cost

for _ in range(0, max(s)+1):
    cost = sum([calc_cost(c, _) for c in s])
    if cost < min_cost:
        min_cost = cost
        lineon = _

print(lineon, min_cost)

#submit(a)

