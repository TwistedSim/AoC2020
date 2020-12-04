import re
from collections import namedtuple

validators = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: (150 <= int(x.replace('cm', '')) <= 193) if 'cm' in x else (59 <= int(x.replace('in', '')) <= 76),
    'hcl': lambda x: len(x) == 7 and re.search(r'\#[a-f0-9]{6}', x) is not None,
    'ecl': lambda x: x in ( 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda x: len(x) == 9 and re.search(r'\d{9}', x) is not None,
    'cid': lambda x: True,
}

def validate_field_count(passport):
    for field in passport:
        if field not in validators.keys():
            return False
    return len(passport) == 8 if 'cid' in passport else len(passport) == 7

def validate_field_value(passport):
    for field, value in passport.items():
        if not validators[field](value):
            return False
    return True

with open('input.txt', 'r') as file:
    raw_data = file.read().split('\n\n')

data = [d.replace('\n', ' ') for d in raw_data]

passports = [
    {field: value for field, value in re.findall(r'(\w+)\:(\S+)', d)} for d in data
]

filtered_passport = list(filter(validate_field_count, passports))
valid_passport = list(filter(validate_field_value, filtered_passport))

# Part 1
print(len(filtered_passport))

# Part 2
print(len(valid_passport))

