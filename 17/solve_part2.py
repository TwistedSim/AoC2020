
from collections import defaultdict, Counter
from copy import deepcopy


def neighbourgs(tx=0, ty=0, tz=0, tw=0):
    for dx, dy, dz, dw in [(i, j, k, l) for i in (-1,0,1) for j in (-1,0,1) for k in (-1,0,1) for l in (-1,0,1) if i != 0 or j != 0 or k != 0 or l != 0]:
        yield tx+dx, ty+dy, tz+dz, tw+dw


def get_adjacent_cells(pocket, tx, ty, tz, tw):
    for x, y, z, w in neighbourgs(tx, ty, tz, tw):
        try:
            yield pocket[w][z][y][x]
        except:
            yield '.'        

def step_part1(pocket):
    new_pocket = deepcopy(pocket)    
    for x, y, z, w in [(x, y, z, w) for w in pocket for z in pocket[w] for y in pocket[w][z] for x in pocket[w][z][y]]:
        state = Counter(get_adjacent_cells(pocket, x, y, z, w))
        if pocket[w][z][y][x] == '#' and state['#'] != 2 and state['#'] != 3:
            new_pocket[w][z][y][x] = '.'
        elif pocket[w][z][y][x] == '.' and state['#'] == 3:
            new_pocket[w][z][y][x] = '#'
        else:
            pass
    return new_pocket


def expand(pocket):
    new_pocket = deepcopy(pocket)
    for x, y, z, w in [(x, y, z, w) for w in pocket for z in pocket[w] for y in pocket[w][z] for x in pocket[w][z][y]]:
        for x, y, z, w in neighbourgs(x, y, z, w):
            try:
                new_pocket[w][z][y][x]
            except:
                new_pocket[w][z][y][x] = '.'
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
pocket = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
for y, row in enumerate(data):
    for x, value in enumerate(row):
        pocket[0][0][y][x] = value

print(pocket)

bootup_pocket = simulate(pocket, step_part1, count=6)

print(Counter(bootup_pocket[w][z][y][x] for w in bootup_pocket for z in bootup_pocket[w] for y in bootup_pocket[w][z] for x in bootup_pocket[w][z][y]))
