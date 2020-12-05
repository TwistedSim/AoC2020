
def compute_uid(row, col):
    return 8*row + col

with open('input.txt', 'r') as file:
    raw_data = file.read().splitlines()

seats = [
    (
        int(d[:7].replace('F', '0').replace('B', '1'), base=2), 
        int(d[7:].replace('L', '0').replace('R', '1'), base=2),
    ) for d in raw_data
]

# Part 1
print(max(compute_uid(row, col) for row, col in seats))

# Part 2

width  = max(seats, key=lambda x: x[0])[0]
height = max(seats, key=lambda x: x[1])[1]

min_row = min(seats, key=lambda x: x[0])[0]

possible_seats = [ (row, col) for col in range(height) for row in range(width) if row > min_row and (row, col) not in seats]

seat = possible_seats[0]
print(seat, compute_uid(*seat))

# Part fun

import pygame 
import time

BLOCK_SIZE = 10

pygame.init()
pygame.display.set_mode([width*BLOCK_SIZE,height*BLOCK_SIZE])
screen = pygame.display.get_surface()

iter_seats = iter(seats)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    seat = next(iter_seats, None)
    if seat:
        row, col = seat 
        screen.fill(pygame.Color(255, 255, 255), pygame.Rect( (row*BLOCK_SIZE, col*BLOCK_SIZE), (BLOCK_SIZE-1, BLOCK_SIZE-1)))
        pygame.display.update()
        
    time.sleep(0.001)

