import re

def get_input():
    with open('input19.txt') as file:
        return [x.strip() for x in file]


def parse_rules(input):
    def process_token(token: str):
        if token.isnumeric():
            return int(token)
        elif token.startswith('"') and token.endswith('"'):
            return token[1:-1]
        else:
            return token

    rules = {}
    for line in input:
        if line == "":
            break

        number, rule = line.split(":")
        tokens = [process_token(x) for x in re.findall('\\d+|\\||(?:\\".\\")', rule)]

        rules[int(number)] = tokens
    return rules

# input = iter([
#     '0: 4 1 5',
#     '1: 2 3 | 3 2',
#     '2: 4 4 | 5 5',
#     '3: 4 5 | 5 4',
#     '4: "a"',
#     '5: "b"',
#     '',
#     'ababbb',
#     'bababa',
#     'abbbab',
#     'aaabbb',
#     'aaaabbb'
# ])


# print(re.fullmatch('a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b', 'ababbb'))
# print(re.fullmatch('a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b', 'abbbab'))
# print(re.fullmatch('a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b', 'bababa'))
# print(re.fullmatch('a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b', 'aaabbb'))
# print(re.fullmatch('a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b', 'aaaabbb'))

input = iter(get_input())
rules = parse_rules(input)
messages = [x for x in input]

def process(rule_id, rules):
    rule = rules[rule_id]
    res = ""
    # print(f"Start {rule_id}")
    for part in rule:
        if type(part)==int:
            res += process(part, rules)
        else:
            res += part

    if "|" in res:
        res = f"(?:{res})"

    # print(f"{rule_id} => {res}")
    return res

e1 = re.compile(process(0, rules))
matches = [e1.fullmatch(x)!=None for x in messages].count(True)

print(f"Number of matches: {matches}")

input = iter([
    '42: 9 14 | 10 1',
    '9: 14 27 | 1 26',
    '10: 23 14 | 28 1',
    '1: "a"',
    '11: 42 31',
    '5: 1 14 | 15 1',
    '19: 14 1 | 14 14',
    '12: 24 14 | 19 1',
    '16: 15 1 | 14 14',
    '31: 14 17 | 1 13',
    '6: 14 14 | 1 14',
    '2: 1 24 | 14 4',
    '0: 8 11',
    '13: 14 3 | 1 12',
    '15: 1 | 14',
    '17: 14 2 | 1 7',
    '23: 25 1 | 22 14',
    '28: 16 1',
    '4: 1 1',
    '20: 14 14 | 1 15',
    '3: 5 14 | 16 1',
    '27: 1 6 | 14 18',
    '14: "b"',
    '21: 14 1 | 1 14',
    '25: 1 1 | 1 14',
    '22: 14 14',
    '8: 42',
    '26: 14 22 | 1 20',
    '18: 15 15',
    '7: 14 5 | 1 21',
    '24: 14 1',
    '',
    'abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa',
    'bbabbbbaabaabba',
    'babbbbaabbbbbabbbbbbaabaaabaaa',
    'aaabbbbbbaaaabaababaabababbabaaabbababababaaa',
    'bbbbbbbaaaabbbbaaabbabaaa',
    'bbbababbbbaaaaaaaabbababaaababaabab',
    'ababaaaaaabaaab',
    'ababaaaaabbbaba',
    'baabbaaaabbaaaababbaababb',
    'abbbbabbbbaaaababbbbbbaaaababb',
    'aaaaabbaabaaaaababaa',
    'aaaabbaaaabbaaa',
    'aaaabbaabbaaaaaaabbbabbbaaabbaabaaa',
    'babaaabbbaaabaababbaabababaaab',
    'aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'
])

input = iter(get_input())
#rules = parse_rules(input)
#messages = [x for x in input]

# rules[8] = [42, '|', 42, 8]
# rules[11] = [42, 31, '|', 42, 11, 31]

r31 = process(31, rules)
r42 = process(42, rules)

def match(x):
    result = re.fullmatch(f"({r42}+)({r31}+)", x)
    if result is not None:
        part1, part2 = result.groups()
        return len(re.split(r42, part1))>len(re.split(r31, part2))

    return False

matches = [match(x) for x in messages].count(True)
print(f"Number of matches: {matches}")
