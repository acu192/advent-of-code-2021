import re, sys, os
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
from itertools import count
#from aocd import submit
#from dateutil.parser import parse


all_sigs = []
all_outs = []


with open('input', 'rt') as f:
    for line in f:
        sigs, outs = line.strip().split(' | ')
        sigs = sigs.split(' ')
        outs = outs.split(' ')
        all_sigs.extend(sigs)
        all_outs.extend(outs)


n_segs = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}

counts = {
    1: 0,
    4: 0,
    7: 0,
    8: 0,
}


for s in all_outs:
    l = len(s)
    if l in n_segs:
        val = n_segs[l]
        counts[val] += 1


total = sum(counts.values())

print(total)

#submit(a)

