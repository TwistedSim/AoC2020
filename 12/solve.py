
from enum import Enum


class Direction(Enum):
    North = ( 1, 0)
    East  = ( 0, 1)
    South = (-1, 0)
    West  = ( 0,-1)

def add(v1, v2):
    return tuple(x1+x2 for x1,x2 in zip(v1,v2))

def diff(v1, v2):
    return tuple(x1-x2 for x1,x2 in zip(v1,v2))

def mult(v, k):
    return tuple(map(lambda x: k*x, v))

def move(position, direction, amount):
    return add(position, mult(direction.value, amount))

def rotate(position, angle):
    return {
          0: ( position[0],  position[1]),
         90: ( position[1], -position[0]),
        180: (-position[0], -position[1]),
        270: (-position[1],  position[0]),
    }[angle % 360]    

def command_to_direction(command):
    return {
        'E': Direction.East,
        'N': Direction.North,
        'W': Direction.West,
        'S': Direction.South,
    }[command]

def angle_to_direction(angle):
    return {
        0:   Direction.East,
        90:  Direction.North,
        180: Direction.West,
        270: Direction.South,
    }[angle % 360]

def manhattan_distance(x, y):
    return abs(x)+abs(y)


with open('input.txt', 'r') as file:
    actions = [(line[0], int(line[1:])) for line in list(file.read().splitlines())]

# Part 1
angle = 0
position = (0, 0)

for action in actions:
    if action[0] in {'N', 'E', 'S', 'W'}:
        position = move(position, command_to_direction(action[0]), action[1])
    elif action[0] == 'L':
        angle += action[1]
    elif action[0] == 'R':
        angle -= action[1]
    elif action[0] == 'F':
        position = move(position, angle_to_direction(angle), action[1])
    else:
        raise ValueError('Invalid action')

print(f'The ferry ended at position {position} pointing {angle_to_direction(angle)}')
print(f'The Manhattan distance from the start position is {manhattan_distance(*position)}')

# Part 2
position = (0, 0)
waypoint = (1, 10)

for action in actions:
    if action[0] in {'N', 'E', 'S', 'W'}:
        waypoint = move(waypoint, command_to_direction(action[0]), action[1])
    elif action[0] == 'L':
        waypoint = rotate(waypoint, action[1])
    elif action[0] == 'R':
        waypoint = rotate(waypoint, -action[1])
    elif action[0] == 'F':
        position = add(position, mult(waypoint, action[1]))
    else:
        raise ValueError('Invalid action')

print(f'The ferry ended at position {position} pointing {angle_to_direction(angle)}')
print(f'The Manhattan distance from the start position is {manhattan_distance(*position)}')
