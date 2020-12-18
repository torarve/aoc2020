import re

def get_input():
    with open('input18.txt') as file:
        return [x.strip() for x in file]


def parse(line):
    current = line
    while current:
        if not current[0].isspace():
            yield current[0]
        current = current[1:]

def calculate(line):
    numbers = []
    operators = []

    def apply_next():
        op = operators.pop()
        if op=='+':
            a = numbers.pop()
            b = numbers.pop()
            numbers.append(a+b)
        elif op=='*':
            a = numbers.pop()
            b = numbers.pop()
            numbers.append(a*b)

    for token in parse(line):
        if token.isdigit():
            numbers.append(int(token))
        elif token==')':
            apply_next()
        else:
            if token!='(' and len(operators)>0:
                apply_next()

            operators.append(token)

    while len(operators)>0:
        apply_next()

    return numbers.pop()

print(calculate("1 + 2 * 3 + 4 * 5 + 6"))
print(calculate("1 + (2 * 3) + (4 * (5 + 6))"))
print(calculate("2 * 3 + (4 * 5)"))
print(calculate("5 + (8 * 3 + 9 + 3 * 4 * 3)"))
print(calculate("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))
print(calculate("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))

print(sum([calculate(x) for x in get_input()]))

def calculate2(line):
    stored = []
    numbers = []
    operators = []
    precedence = { '+': 2, '*': 1}

    def apply_next():
        op = operators.pop()
        if op=='+':
            a = numbers.pop()
            b = numbers.pop()
            numbers.append(a+b)
        elif op=='*':
            a = numbers.pop()
            b = numbers.pop()
            numbers.append(a*b)

    for token in parse(line):
        if token.isdigit():
            numbers.append(int(token))
        elif token==')':
            while len(operators)>0:
                apply_next()
            res = numbers.pop()
            numbers, operators = stored.pop()
            numbers.append(res)
        elif token=='(':
            stored.append((numbers, operators))
            numbers = []
            operators = []
        else:
            if len(operators)>0:
                while len(operators)>0 and precedence[token]<precedence[operators[-1]]:
                    apply_next()

            operators.append(token)

    while len(operators)>0:
        apply_next()

    return numbers.pop()

print(calculate2("1 + 2 * 3 + 4 * 5 + 6"))
print(calculate2("1 + (2 * 3) + (4 * (5 + 6))"))
print(calculate2("2 * 3 + (4 * 5)"))
print(calculate2("5 + (8 * 3 + 9 + 3 * 4 * 3)"))
print(calculate2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))
print(calculate2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))

print(sum([calculate2(x) for x in get_input()]))