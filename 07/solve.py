from operator import mul
from functools import reduce

from anytree import Node, RenderTree, PreOrderIter
from anytree.search import findall_by_attr
from anytree.walker import Walker

from collections import defaultdict, Counter


def find_roots(rules):
    counter = Counter(bag for bag in rules) + Counter(c[1] for content in rules.values() for c in content)
    return list(counter.keys())


def generate_subtree(rules, parent, content):
    for c in content:
        number, bag = c
        children = Node(bag, count=number, parent=parent)
        generate_subtree(rules, children, rules[bag])


def generate_rules_tree(rules, root):
    parent = Node(root, count=1)
    generate_subtree(rules, parent, rules[root])
    return parent


def recursive_sum(node):
    if node.children:        
        return node.count*(1 + sum(recursive_sum(child) for child in node.children))
    return node.count


def display_tree(tree):    
    for pre, fill, node in RenderTree(rules_tree):
        print("%s%s (%d)" % (pre, node.name, node.count))


with open('input.txt', 'r') as file:
    data = (line for line in file.read().splitlines())
    data = (d.split('contain') for d in data)
    data = ((bag.strip().replace(' bags', '').replace(' bag', ''), content.strip().replace('.', '').split(', ')) for bag, content in data)


rules = defaultdict(list)
for rule in data:
    bag, contents = rule
    for c in contents:
        if c != 'no other bags':
            rule = c.split(' ', 1)
            rule[0] = int(rule[0])
            rule[1] = rule[1].replace(' bags', '').replace(' bag', '')
            rules[bag].append(tuple(rule))

# Part 1
shiny_bag_count = 0
for root in find_roots(rules):
    rules_tree = generate_rules_tree(rules, root)
    nodes = findall_by_attr(rules_tree, 'shiny gold')
    if root != 'shiny gold' and nodes:
        shiny_bag_count += 1
print(shiny_bag_count)

# Part 2
rules_tree = generate_rules_tree(rules, 'shiny gold')
#display_tree(rules_tree)
print(recursive_sum(rules_tree)-1)