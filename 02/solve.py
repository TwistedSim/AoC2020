
from collections import namedtuple

Password = namedtuple('Password', 'password, letter, min, max')

def validate(item):
    return item.min <= item.password.count(item.letter) <= item.max

def validate_new(item):
    return (item.password[item.min-1] == item.letter) ^ (item.password[item.max-1] == item.letter)

with open('input.txt', 'r') as file:
    data = list(file.read().strip().split('\n'))

passwords = [
    Password(
         min = int(d.split('-')[0]),
         max = int(d.split('-')[1].split(' ')[0]),
        password = d.split(': ')[1],
          letter = d.split(':')[0].split(' ')[1]
     ) for d in data
]

print(len(list(filter(validate, passwords))))
print(len(list(filter(validate_new, passwords))))

