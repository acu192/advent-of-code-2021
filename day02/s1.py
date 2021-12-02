import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
#from dateutil.parser import parse

x = 0

y = 0

with open('input', 'rt') as f:
    s = f.read().strip().splitlines()
    dirs = [l.split() for l in s]

for i, n in dirs:
    if i == 'forward':
        x += int(n)
    elif i == 'down':
        y += int(n)
    elif i == 'up':
        y -= int(n)
    else:
        raise Exception('!')

print(x, y, x * y)

