import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
#from dateutil.parser import parse


with open('input', 'rt') as f:
    vals = [list(l) for l in f.read().splitlines()]

gamma = []
eps = []

for c in range(len(vals[0])):
    col = [vals[i][c] for i in range(len(vals))]
    most_common = Counter(col).most_common(1)[0][0]
    gamma.append(most_common)
    eps.append(str(1 - int(most_common)))

gamma = ''.join(gamma)
eps = ''.join(eps)

gamma = int(gamma, 2)
eps = int(eps, 2)

print(gamma, eps, gamma * eps)

#print(vals)

print(a)
#submit(a)

