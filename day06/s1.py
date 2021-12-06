import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
#from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    s = [int(v) for v in f.read().strip().split(',')]


for d in range(1, 81):
    for i, v in enumerate(list(s)):
        if v == 0:
            s[i] = 6
            s.append(8)
        else:
            s[i] -= 1

print(len(s))

#submit(a)

