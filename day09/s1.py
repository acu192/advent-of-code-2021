import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
#from aocd import submit
#from dateutil.parser import parse


with open('input', 'rt') as f:
    map = [[int(ch) for ch in line] for line in f.read().strip().splitlines()]

def adj(i, j):
    if i > 0:
        yield i-1, j
    if i + 1 < len(map):
        yield i+1, j
    if j > 0:
        yield i, j-1
    if j + 1 < len(map[i]):
        yield i, j+1

risk = 0

for i in range(len(map)):
    row = map[i]
    for j in range(len(row)):
        n_lower = 0
        n_adj = 0
        for dx, dy in adj(i, j):
            if map[dx][dy] > map[i][j]:
                n_lower += 1
            n_adj += 1
        if n_lower == n_adj:
            risk += map[i][j] + 1

print(risk)

