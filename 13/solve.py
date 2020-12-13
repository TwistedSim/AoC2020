
from scipy.optimize import fsolve
from operator import mul
from functools import reduce

depart_time = 1015292
data = '19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,743,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,643,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23'

# Part 1
schedule = [int(x) for x in data.split(',') if x != 'x']
closest_bus = min(map(lambda x: (x - (depart_time % x), x), schedule))
print(reduce(mul, closest_bus))

# Part 2

def crt(n, a):
    s = 0
    prod = reduce(mul, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        s += a_i * modinv(p, n_i) * p
    return s % prod

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

schedule = [(int(x), -idx) for idx, x in enumerate(data.split(',')) if x != 'x']
print(crt(*zip(*schedule)))