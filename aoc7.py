import re

def get_input():
    with open('input7.txt') as file:
        return [x.strip() for x in file]

def parse_bag_string(bags):
    m = re.fullmatch("(\\d+) (.*?)s?", bags)
    if m is None:
        return (0, '')
    
    x, y = m.groups()
    return int(x), y

def parse_line(line):
    line = line.strip(".")
    a, b = line.split(" contain ")
    if a[-1] == 's':
        a = a[:-1]

    b = [parse_bag_string(x) for x in b.split(", ")]
    return (a,b)

rules = get_input()

def can_contain(type_of_bag):
    for rule in rules:
        a, b = parse_line(rule)
        for i in b:
            if i != None:
                if type_of_bag == i[-1]:
                    yield a

current = set(["shiny gold bag"])
done = set()
result = set()

while len(current) > 0:
    what = current.pop()
    for i in can_contain(what):
        result.add(i)
        if i not in done:
            current.add(i)
    done.add(what)


print(len(result))
# print(list(can_contain("shiny gold bag")))
# print(count1)

def find_rule_for(name):
    for rule in rules:
        if rule[0]==name:
            return rule
    return None

rules = [parse_line(line) for line in rules]
rules = dict(rules)
rule = rules["shiny gold bag"]

def num_bags_inside(name):
    if name not in rules.keys():
        return 0
    
    contents = rules[name]
    if len(contents) == 0:
        return 0

    print(name)
    result = [count*(num_bags_inside(name)+1) for count, name in contents]
    print(result)
    return sum(result)


current = set(rule)
done = set()
result = 0

# while len(current) > 0:
#     count, name = current.pop()
#     result = result + count
#     for i in rules[name]:
#         if i is not None:
#             current.add(i)

# print(result)

print(num_bags_inside("shiny gold bag"))

#print(rule)
