import re

def read_input():
    with open("input2.txt") as file:
        return [x.strip() for x in file.readlines()]

def is_valid_part1(line):
    m = re.match("(\\d+)-(\\d+) (\\w): (.+)", line)
    lower, upper, char, password = m.groups()
    count = password.count(char)
    return count>=int(lower) and count <= int(upper)

def is_valid_part2(line):
    m = re.match("(\\d+)-(\\d+) (\\w): (.+)", line)
    first, second, char, password = m.groups()
    first_pos = int(first) - 1
    second_pos = int(second) - 1
    return (password[first_pos]==char) ^ (password[second_pos]==char)

lines = read_input()

valid_passwords_part1 = [x for x in lines if is_valid_part1(x)]
print(f"Valid passwords (part 1): {len(valid_passwords_part1)}")

valid_passwords_part2 = [x for x in lines if is_valid_part2(x)]
print(f"Valid passwords (part 2): {len(valid_passwords_part2)}")
