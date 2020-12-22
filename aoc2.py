import re

def read_input():
    with open("input2.txt") as file:
        return [x.strip() for x in file.readlines()]

def parse_line(line):
    m = re.match("(\\d+)-(\\d+) (\\w): (.+)", line)
    first, second, char, password = m.groups()
    return int(first), int(second), char, password

def is_valid_part1(line):
    lower, upper, char, password = parse_line(line)
    count = password.count(char)
    return count>=int(lower) and count <= int(upper)

def is_valid_part2(line):
    first, second, char, password = parse_line(line)
    return (password[first-1]==char) ^ (password[second-1]==char)

lines = read_input()

valid_passwords_part1 = [x for x in lines if is_valid_part1(x)]
print(f"Valid passwords (part 1): {len(valid_passwords_part1)}")

valid_passwords_part2 = [x for x in lines if is_valid_part2(x)]
print(f"Valid passwords (part 2): {len(valid_passwords_part2)}")
