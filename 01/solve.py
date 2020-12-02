import math 
import time

def find_pair(data, target):
    pairs = {}
    for d in data:
        if d in pairs:
            if pairs[d] != None:
                yield tuple(sorted((d, target-d)))
            pairs[target-d] = None
        elif d not in pairs.values():
            pairs[target-d] = d

def find_triplet(data, target):
    triplets = set()
    for d in data:
        for p1, p2 in find_pair(data, target-d):
            t = tuple(sorted((d, p1, p2)))
            if t not in triplets:
                yield t
                triplets.add(t)

with open('input.txt', 'r') as file:
    data = list(map(int, file.read().strip().split('\n')))

print(*(k[0]*k[1] for k in find_pair(data, 2020)))
print(*(k[0]*k[1]*k[2] for k in find_triplet(data, 2020)))

