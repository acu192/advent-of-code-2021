import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
#from dateutil.parser import parse


with open('input', 'rt') as f:
    s = f.read().strip()
    parts = s.split('\n\n')

calls = parts[0]

calls = [int(v) for v in calls.split(',')]

boards = parts[1:]

def parseBoard(b):
    rows = b.strip().splitlines()
    return [[[int(v), False] for v in r.split(' ') if v] for r in rows]

boards = [parseBoard(b) for b in boards]

def checkWinner(bs):
    for i, b in enumerate(bs):
        for row in b:
            all_ = True
            for col in row:
                if not col[1]:
                    all_ = False
            if all_:
                return i
        b2 = [[b[i][j] for i in range(len(b))] for j in range(len(b))]
        for row in b2:
            all_ = True
            for col in row:
                if not col[1]:
                    all_ = False
            if all_:
                return i

for c in calls:
    for b in boards:
        for row in b:
            for col in row:
                if col[0] == c:
                    col[1] = True
    winner = checkWinner(boards)
    if winner is not None:
        break

winning_board = boards[winner]
s = 0
for row in winning_board:
    for col in row:
        if not col[1]:
            s += col[0]

print(s * c)

