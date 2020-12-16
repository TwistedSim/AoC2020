import re

def apply_bitmask(mask, n):
    base2 = f"{n:0>36b}"
    return int(''.join(m if m != 'X' else b for m, b in zip(mask, base2)), base=2)


def apply_bitmask_v2(mask, n):
    base2 = f"{n:0>36b}"
    return ''.join(b if m == '0' else '1' if m == '1' else 'X' for m, b in zip(mask, base2))


def collapse(address_space):
    x_count = address_space.count('X')    
    for p in range(2**x_count):
        base2 = iter(f"{p:0>{x_count}b}")  # voodoo magic
        yield int(''.join(a if a != 'X' else next(base2) for a in address_space), base=2)


with open('input.txt') as file:
    instructions = file.read().splitlines()

# Part 1

memory = {}
current_mask = None

for instr in instructions:
    if instr.startswith('mask'):
        current_mask = re.search(r'mask = ([X01]+)', instr).group(1)
    else:
        address, value = re.search(r'\[(\d+)\] = (\d+)', instr).groups()
        memory[int(address)] = apply_bitmask(current_mask, int(value))

print(sum(memory.values()))

# Part 2

memory = {}
current_mask = None

for instr in instructions:
    if instr.startswith('mask'):
        current_mask = re.search(r'mask = ([X01]+)', instr).group(1)
    else:
        address, value = re.search(r'\[(\d+)\] = (\d+)', instr).groups()
        address_space = apply_bitmask_v2(current_mask, int(address))
        for address in collapse(address_space):
            memory[int(address)] = int(value)

print(sum(memory.values()))