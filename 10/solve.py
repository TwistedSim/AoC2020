from collections import Counter
from functools import reduce
from operator import mul

with open('input.txt', 'r') as file:
    adapters = list(map(int, file.read().splitlines()))

chargin_outlet = 0 
builtin_adapter = max(adapters)+3

# Part 1
adapters_series = sorted(adapters)
adapters_series.insert(0, chargin_outlet)
adapters_series.append(builtin_adapter)

diff = [a2-a1 for a1, a2 in zip(adapters_series, adapters_series[1:])]
difference_count = Counter(diff)

print(difference_count)

print(difference_count[1]*difference_count[3])

#Part 2
def tribonacci(n) :
    if n <= 0:
        return 1
    if n in {0,1,2}:
        return [1,2,4][n]
    else :
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)


pos_3 = [i for i, x in enumerate(diff) if x == 3]
pos_3.insert(0, -1)
print(reduce(mul, map(tribonacci, [p2-p1-2 for p1, p2 in zip(pos_3, pos_3[1:])])))