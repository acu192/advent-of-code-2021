import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
#from dateutil.parser import parse

pos = 0

aim = 0

dep = 0

with open('input', 'rt') as f:
    s = f.read().strip().splitlines()
    dirs = [l.split() for l in s]

for i, n in dirs:
    if i == 'forward':
        pos += int(n)
        dep += aim * int(n)
    elif i == 'down':
        aim += int(n)
    elif i == 'up':
        aim -= int(n)
    else:
        raise Exception('!')

print(pos, aim, dep, pos * dep)

