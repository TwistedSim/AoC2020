from collections import Counter
from functools import reduce
from copy import deepcopy

def display(seats):
    print()
    print(*['  ' + ''.join(row) for row in seats], sep='\n')
    print()


def compare(s1, s2):
    return reduce(lambda i, j : i and j, map(lambda m, k: m == k, s1, s2), True)


def is_valid(seats, x, y):
    return 0 <= x < len(seats[0]) and 0 <= y < len(seats)

def get_adjacent_cells(seats, tx, ty):
    for x, y in [(tx+i, ty+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
        if is_valid(seats, x, y):
            yield seats[y][x]


def step_part1(seats):
    new_seats = deepcopy(seats)
    for x, y in [(i, j) for i in range(len(seats[0])) for j in range(len(seats))]:
        state = Counter(get_adjacent_cells(seats, x, y))
        if seats[y][x] == 'L' and state['#'] == 0:
            new_seats[y][x] = '#'
        elif seats[y][x] == '#' and state['#'] >= 4:
            new_seats[y][x] = 'L'
        else:
            pass
    return new_seats


def get_view_cells(seats, tx, ty):
    for dx, dy in [(i, j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
        sx, sy = tx, ty
        while is_valid(seats, sx+dx, sy+dy):
            sx += dx
            sy += dy
            if seats[sy][sx] != '.':
                yield seats[sy][sx]
                break

def step_part2(seats):
    new_seats = deepcopy(seats)
    for x, y in [(i, j) for i in range(len(seats[0])) for j in range(len(seats))]:
        state = Counter(get_view_cells(seats, x, y))        
        if seats[y][x] == 'L' and state['#'] == 0:
            new_seats[y][x] = '#'
        elif seats[y][x] == '#' and state['#'] >= 5:
            new_seats[y][x] = 'L'
        else:
            pass
    return new_seats


def simulate(seats, step):
    while True:
        new_seats = step(seats)
        if compare(new_seats, seats):
            print('Simulation is over')
            print('There are ', Counter([s for row in seats for s in row])['#'], 'occupied seats')
            break
        yield new_seats
        seats = deepcopy(new_seats)


with open('input.txt', 'r') as file:
    seats = [[elt for elt in line] for line in list(file.read().splitlines())]


for s in simulate(seats, step_part1):
    #display(s)
    pass

for idx, s in enumerate(simulate(seats, step_part2)):
    display(s)
    pass