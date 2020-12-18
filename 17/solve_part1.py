
from collections import defaultdict, Counter
from copy import deepcopy


def neighbourgs(tx=0, ty=0, tz=0):
    for dx, dy, dz in [(i, j, k) for i in (-1,0,1) for j in (-1,0,1) for k in (-1,0,1) if i != 0 or j != 0 or k != 0]:
        yield tx+dx, ty+dy, tz+dz


def get_adjacent_cells(pocket, tx, ty, tz):
    for x, y, z in neighbourgs(tx, ty, tz):
        try:
            yield pocket[z][y][x]
        except:
            yield '.'        

def step_part1(pocket):
    new_pocket = deepcopy(pocket)    
    for x, y, z in [(x, y, z) for z in pocket for y in pocket[z] for x in pocket[z][y]]:
        state = Counter(get_adjacent_cells(pocket, x, y, z))
        if pocket[z][y][x] == '#' and state['#'] != 2 and state['#'] != 3:
            new_pocket[z][y][x] = '.'
        elif pocket[z][y][x] == '.' and state['#'] == 3:
            new_pocket[z][y][x] = '#'
        else:
            pass
    return new_pocket


def expand(pocket):
    new_pocket = deepcopy(pocket)
    for x, y, z in [(x, y, z) for z in pocket for y in pocket[z] for x in pocket[z][y]]:
        for x, y, z in neighbourgs(x, y, z):
            try:
                new_pocket[z][y][x]
            except:
                new_pocket[z][y][x] = '.'
    return new_pocket

def simulate(pocket, step, count):
    for _ in range(count):
        pocket = expand(pocket)
        pocket = step(pocket)
    return pocket

puzzle_input = """
##.#####
#.##..#.
.##...##
###.#...
.#######
##....##
###.###.
.#.#.#..
"""

data = [[elt for elt in line] for line in puzzle_input.strip().split()]

# pocket[z][y][x]
pocket = defaultdict(lambda: defaultdict(dict))
for y, row in enumerate(data):
    for x, value in enumerate(row):
        pocket[0][y][x] = value

print(pocket)

bootup_pocket = simulate(pocket, step_part1, count=6)

print(Counter(bootup_pocket[z][y][x] for z in bootup_pocket for y in bootup_pocket[z] for x in bootup_pocket[z][y]))
