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

cache = {}

def find_basin(i, j):
    if map[i][j] == 9:
        return

    if (i, j) in cache and cache[(i, j)] != 'finding':
        return cache[(i, j)]
    n_lower = 0
    n_adj = 0
    for dx, dy in adj(i, j):
        if map[dx][dy] > map[i][j]:
            n_lower += 1
        n_adj += 1
    if n_lower == n_adj:
        cache[(i, j)] = (i, j)  # we are our own basin
        return (i, j)

    cache[(i, j)] = 'finding'

    for dx, dy in adj(i, j):
        if map[dx][dy] <= map[i][j]:
            if (dx, dy) in cache and cache[(dx, dy)] == 'finding':
                continue
            ans = find_basin(dx, dy)
            cache[(i, j)] = ans
            return ans

    raise Exception('unreachable')

for i, row in enumerate(map):
    for j, val in enumerate(row):
        find_basin(i, j)

vals = Counter(cache.values())

ans = 1

for (i, j), count in vals.most_common(3):
    ans *= count

print(ans)

