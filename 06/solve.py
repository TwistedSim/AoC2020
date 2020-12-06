
with open('input.txt', 'r') as file:
    data = [d.strip().split() for d in file.read().split('\n\n')]

# Part 1
print(sum(len(set(answer for people in decl for answer in people)) for decl in data))

# Part 2
print(sum(len(set.intersection(*map(set, decl))) for decl in data))