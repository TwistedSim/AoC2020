import re
from collections import namedtuple

Password = namedtuple('Password', 'password, letter, min, max')

def validate(item):
    return item.min <= item.password.count(item.letter) <= item.max

def validate_new(item):
    return (item.password[item.min-1] == item.letter) ^ (item.password[item.max-1] == item.letter)

with open('input.txt', 'r') as file:
    raw_data = file.read().strip()

pattern = re.compile(r'([0-9]+)\-([0-9]+)\s([a-z])\:\s([a-z]+)')

passwords = [
    Password(password, letter, int(min_), int(max_)) 
    for min_, max_, letter, password in re.findall(pattern, raw_data)
]

print(len(list(filter(validate, passwords))))
print(len(list(filter(validate_new, passwords))))

