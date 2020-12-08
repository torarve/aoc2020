import re

def is_valid_part2(line):
    m = re.match("(\\d+)-(\\d+) (\\w): (.+)", line)
    first, second, char, password = m.groups()
    first_pos = int(first) - 1
    second_pos = int(second) - 1
    return (password[first_pos]==char) ^ (password[second_pos]==char)

def is_valid_part1(line):
    m = re.match("(\\d+)-(\\d+) (\\w): (.+)", line)
    lower, upper, char, password = m.groups()
    count = password.count(char)
    return count>=int(lower) and count <= int(upper)

lines = None
with open("input2.txt") as file:
    lines = [x.strip() for x in file.readlines()]

lines = [x for x in lines if is_valid_part1(x)]
print(len(lines))

lines = [x for x in lines if is_valid_part2(x)]
print(len(lines))
