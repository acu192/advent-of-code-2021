import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
from aocd import submit
#from dateutil.parser import parse


prev = None
c = 0

with open('input', 'rt') as f:
    for line in f:
        here = int(line)
        if prev is None:
            pass
        else:
            if prev < here:
                c += 1
        prev = here


print(c)
#submit(a)

