import enum
import re
import operator

# Stolen form https://github.com/gnebehay/parser/blob/master/parser.py

import enum
import re


class TokenType(enum.Enum):
    T_NUM = 0
    T_PLUS = 1
    T_MINUS = 2
    T_MULT = 3
    T_DIV = 4
    T_LPAR = 5
    T_RPAR = 6
    T_START = 7


class Node:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value
        self.children = []


def lexical_analysis(s):
    mappings = {
        '+': TokenType.T_PLUS,
        '-': TokenType.T_MINUS,
        '*': TokenType.T_MULT,
        '/': TokenType.T_DIV,
        '(': TokenType.T_LPAR,
        ')': TokenType.T_RPAR}

    tokens = []
    for c in s:
        if c == ' ':
            continue
        elif c in mappings:
            token_type = mappings[c]
            token = Node(token_type, value=c)
        elif re.match(r'\d+', c):
            token = Node(TokenType.T_NUM, value=int(c))
        else:
            raise Exception('Invalid token: {}'.format(c))
        tokens.append(token)
    tokens.insert(0, Node(TokenType.T_START))
    return tokens


def match(tokens, token):
    if tokens[-1].token_type == token:
        return tokens.pop()
    else:
        raise_syntax_error(tokens)


def parse_e(tokens):
    return parse_ea(tokens, parse_e3(tokens),)


def parse_ea(tokens, left_node):
    if tokens[-1].token_type in {TokenType.T_PLUS, TokenType.T_MINUS, TokenType.T_MULT, TokenType.T_DIV}:
        node = tokens.pop()
        node.children.append(left_node)
        node.children.append(parse_e(tokens))
        return node
    elif tokens[-1].token_type in [TokenType.T_LPAR, TokenType.T_START]:
        return left_node
    raise_syntax_error(tokens)


def parse_e3(tokens):
    if tokens[-1].token_type == TokenType.T_NUM:
        return tokens.pop()
    match(tokens, TokenType.T_RPAR)
    e_node = parse_e(tokens)
    match(tokens, TokenType.T_LPAR)
    return e_node


def raise_syntax_error(tokens):
    raise Exception('Invalid syntax on token {}'.format(tokens[-1].token_type))


def parse(inputstring):
    tokens = lexical_analysis(inputstring)
    ast = parse_e(tokens)
    match(tokens, TokenType.T_START)
    return ast


operations = {
    TokenType.T_PLUS: operator.add,
    TokenType.T_MINUS: operator.sub,
    TokenType.T_MULT: operator.mul,
    TokenType.T_DIV: operator.truediv
}


def compute(node):
    if node.token_type == TokenType.T_NUM:
        return node.value
    left_result = compute(node.children[0])
    right_result = compute(node.children[1])
    operation = operations[node.token_type]
    return operation(left_result, right_result)


with open('input.txt') as file:
    problems = file.read().splitlines()


print(sum(compute(parse(p)) for p in problems))
