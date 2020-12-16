import re

def get_input():
    with open('input16.txt') as file:
        return [x.strip() for x in file]

def parse_rule(line):
    m = re.fullmatch("(.*): (\\d+)-(\\d+) or (\\d+)-(\\d+)", line)
    name, s1, e1, s2, e2 = m.groups()
    return (name, int(s1), int(e1), int(s2), int(e2))

def read_rules(lines):
    for line in lines:
        if line != "":
            yield parse_rule(line)
        else:
            break

def read_nearby_tickets(lines):
    skip = True
    for line in lines:
        if line == "nearby tickets:":
            skip = False
        elif not skip:
            yield [int(x) for x in line.split(",")]

def read_my_ticket(lines):
    skip = True
    for line in lines:
        if line == 'your ticket:':
            skip = False
        elif not skip:
            return [int(x) for x in line.split(",")]

lines = get_input()

rules = [x for x in read_rules(lines)]
my_ticket = read_my_ticket(lines)
nearby_tickets = [x for x in read_nearby_tickets(lines)]

def is_valid_for(value, rule):
    name, s1, e1, s2, e2 = rule
    if (value < s1 or value > e1) and (value < s2 or value > e2):
        return False

    return True

values = []
for ticket in nearby_tickets:
    for value in ticket:
        values.append(value)

invalid_values = []
for value in values:
    tmp = [is_valid_for(value, rule) for rule in rules]
    if tmp.count(True)==0:
        invalid_values.append(value)

print(sum(invalid_values))


def is_valid_ticket(ticket, rules):
    for value in ticket:
        tmp = [is_valid_for(value, rule) for rule in rules]
        if tmp.count(True)==0:
            return False
    return True


# rules = [ ('class', 0, 1, 4, 19), ('row', 0, 5, 8, 19), ('seat', 0, 13, 16, 19)]
# my_ticket = (11, 12, 13)
# nearby_tickets = [(3,9,18), (15,1,5), (5, 14, 9)]

tickets = list(filter(lambda x: is_valid_ticket(x, rules), nearby_tickets))
tickets.append(my_ticket)

fields = set([x[0] for x in rules])
solution = [fields]*len(my_ticket)

for ticket in tickets:
    for i, value in enumerate(ticket):
        tmp = set([rule[0] for rule in rules if is_valid_for(value, rule)])
        solution[i] = solution[i].intersection(tmp)


def is_single_solution(solution):
    return len([x for x in solution if len(x)>1])==0

while not is_single_solution(solution):
    i = i + 1
    for s in solution:
        if len(s) == 1:
            for t in solution:
                if s!=t:
                    t.difference_update(s)
        else:
            updated_s = set(s)
            for field in s:
                tmp = [x for x in solution if x!=s and field in x]
                if len(tmp)==0:
                    updated_s = set([field])
            s.intersection_update(updated_s)

result = 1
for field, value in zip([x.pop() for x in solution], my_ticket):
    if field.startswith("departure"):
        result *= value

print(result)