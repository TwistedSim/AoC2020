from operator import mul
from functools import reduce

def add(vec1, vec2):
    return [v1+v2 for v1,v2 in zip(vec1, vec2)]

def test_slope(tree_map, slope):
    pos = [0, 0]
    tree = 0

    height, length = len(tree_map), len(tree_map[0])
    while pos[1] < height:
        if tree_map[pos[1]][pos[0]]:
            tree += 1
        pos = add(pos, slope)
        pos[0] %= length

    return tree

with open('input.txt', 'r') as file:
    raw_data = file.read().splitlines()

tree_map = [[False if elt == '.' else True for elt in line] for line in raw_data]

# Part 1
print(test_slope(tree_map, (3, 1)))

# Part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = [test_slope(tree_map, s) for s in slopes]
print(reduce(mul, trees))