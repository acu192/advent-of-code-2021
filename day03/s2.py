import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
#from dateutil.parser import parse


with open('input', 'rt') as f:
    vals = [list(l) for l in f.read().splitlines()]

n_cols = len(vals[0])

vals2 = vals

for c in range(n_cols):
    if len(vals2) == 1:
        break
    col = [vals2[i][c] for i in range(len(vals2))]
    ctr = Counter(col).most_common(2)
    most_common = ctr[0][0]
    if ctr[0][1] == ctr[1][1]:
        most_common = '1'
    vals2 = [v for v in vals2 if v[c] == most_common]

assert len(vals2) == 1

print(vals2[0])

ox = int(''.join(vals2[0]), 2)

vals2 = vals

for c in range(n_cols):
    if len(vals2) == 1:
        break
    col = [vals2[i][c] for i in range(len(vals2))]
    ctr = Counter(col).most_common(2)
    most_common = ctr[0][0]
    if ctr[0][1] == ctr[1][1]:
        most_common = '1'
    least_common = str(1 - int(most_common))
    vals2 = [v for v in vals2 if v[c] == least_common]

assert len(vals2) == 1

print(vals2[0])

co2 = int(''.join(vals2[0]), 2)

print(ox, co2, ox * co2)

