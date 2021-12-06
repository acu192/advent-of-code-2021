import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
#from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    s = [int(v) for v in f.read().strip().split(',')]


counts = {}

for i in range(0, 9):
    counts[i] = 0

for v in s:
    counts[v] += 1

for d in range(1, 257):
    orig_zero = counts[0]
    counts[0] = counts[1]
    counts[1] = counts[2]
    counts[2] = counts[3]
    counts[3] = counts[4]
    counts[4] = counts[5]
    counts[5] = counts[6]
    counts[6] = counts[7] + orig_zero
    counts[7] = counts[8]
    counts[8] = orig_zero

total = 0

for v, c in counts.items():
    total += c

print(total)
