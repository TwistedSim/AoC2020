import re


with open('input.txt') as file:
    sections = file.read().split('\n\n')


# Look at my awful parsing!

rules = [rule for rule in sections[0].splitlines()]
my_ticket = list(map(int, sections[1].splitlines()[1].split(',')))
other_tickets = list(map(lambda x: list(map(int, x.split(','))), sections[2].splitlines()[1:]))

create_range = lambda x: range(int(x.strip().split('-')[0]), int(x.strip().split('-')[1])+1)
rules = [
    {
        'name': r.split(':')[0],
        'ranges': [create_range(x) for x in r.split(':')[1].split(' or ')]
    } for r in rules
]

# Part 1
valid_tickets = []
invalid_value_count = 0
for ticket in other_tickets:
    is_valid = True
    for value in ticket:
        if all(not any(value in r for r in rule['ranges']) for rule in rules):
            is_valid = False
            invalid_value_count += value
    if is_valid:
        valid_tickets.append(ticket)

print(invalid_value_count)

# Part 2

from collections import defaultdict
from operator import mul
from functools import reduce

# find every possible match
rules_match = defaultdict(set)
for idx, field in enumerate(zip(*valid_tickets)):
    for rule in rules:       
        if all(any(value in r for r in rule['ranges']) for value in field):
            #  print(f'Match found for rule {rule["name"]} at index {idx}')
            rules_match[rule["name"]].add(idx)


# Match the rules uniquely

rules_position = {}
position = 0
while any(len(m) > 0 for m in rules_match.values()):
    name, positions = next(filter(lambda x: len(x[1])==1, rules_match.items()))    
    pos = positions.pop()
    rules_position[pos] = name
    for m in rules_match.values():
        m.discard(pos)

print(*sorted(rules_position.items()), sep='\n')

print(reduce(mul, (my_ticket[pos] for pos, name in filter(lambda x: x[1].startswith('departure'), rules_position.items()))))