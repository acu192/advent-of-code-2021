import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


lst = []

with open('input', 'rt') as f:
    for line in f:
        here = int(line)
        lst.append(here)


c = 0

for i in range(1, len(lst)-2):
    prev = lst[i-1] + lst[i] + lst[i+1]
    here = lst[i] + lst[i+1] + lst[i+2]
    if here > prev:
        c += 1


print(c)
#submit(a)

