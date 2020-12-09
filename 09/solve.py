from itertools import islice

def window(seq, n=2):
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

def find_pair(data, target):
    pairs = {}
    for d in data:
        if d in pairs:
            if pairs[d] != None:
                yield tuple(sorted((d, target-d)))
            pairs[target-d] = None
        elif d not in pairs.values():
            pairs[target-d] = d


with open('input.txt', 'r') as file:
    cipher = list(map(int, file.read().splitlines()))

preambule = 25
weakness = None

for idx, w in enumerate(window(cipher, n=preambule+1)):
    if idx < preambule:
        continue
    for p in find_pair(w[:-1], w[-1]):
        if len(set(p)) > 1:
            break
    else:
        print()
        print(f'No pair found at {idx} for {w[-1]}')
        print()
        weakness = w[-1]
        break

if not weakness:
    print('No weakness point found')
    print()
else:
    weaks = []
    for c in cipher:
        weaks.append(c)   
        while sum(weaks) > weakness:
            weaks.pop(0)
        if sum(weaks) == weakness and len(weaks) > 1:
            print(f'Range found. Target={weakness}, Range={weaks}')
            print()
            print(f'Answer: {min(weaks)+max(weaks)}')
                





