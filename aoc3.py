import itertools

def read_input():
    with open("input3.txt") as file:
        return [x.strip() for x in file.readlines()]

def get_at(pos, line):
    pos = pos % len(line)
    return line[pos]

def is_tree(square):
    return square=="#"

def number_of_collisions(step_x, step_y=1):
    lines = read_input()
    squares = map(get_at, itertools.count(step=step_x), lines[::step_y])
    hits = filter(is_tree, squares)
    return len(list(hits))

print(f"Answer to part 1: {number_of_collisions(3)}")

a, b, c, d, e = (
    number_of_collisions(1),
    number_of_collisions(3),
    number_of_collisions(5),
    number_of_collisions(7),
    number_of_collisions(1,2))

print(f"Answer to part 2: {a*b*c*d*e}")