
from itertools import count
from collections import defaultdict


def game(starting_number):
    sequence = defaultdict(list)
    for idx, s in enumerate(starting_number):
        sequence[s].append(idx)

    yield from starting_number

    spoken_number = starting_number[-1]
    for turn in count(len(starting_number)):       
        if sequence[spoken_number][0] != turn-1:   
            spoken_number = (turn-1) - sequence[spoken_number][-2]
        else:
            spoken_number = 0        
        
        if len(sequence[spoken_number]) > 1:
            sequence[spoken_number][0] = sequence[spoken_number][1]
            sequence[spoken_number][1] = turn
        else:
            sequence[spoken_number].append(turn)

        yield spoken_number

starting_number = [7,12,1,0,16,2]

for turn_number, spoken_number in enumerate(game(starting_number)):        
    if turn_number == 30000000-1:
        print(spoken_number)
        break