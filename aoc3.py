import itertools


def read_input():
    with open("input3.txt") as file:
        return [x.strip() for x in file.readlines()]

lines = read_input()

def try1():
    line_size = max(map(lambda x: len(x), lines))
    num_lines = len(lines)
    positions = [(x*3)%line_size for x in range(0, num_lines-1)]

    #print(line_size)
    #print(positions)
    # print(lines)
    squares = list(map(lambda pos, line: line[pos], positions, lines))
    #print(squares)
    hits = list(filter(lambda x: x=="#", squares))

    print(len(hits))

def get_square(pos, line):
    pos = pos % len(line)
    return line[pos]

def is_tree(square):
    return square=="#"

def number_of_hits(step_x, step_y=1):
    squares = map(get_square, itertools.count(step=step_x), lines[::step_y])
    hits = filter(is_tree, squares)
    return len(list(hits))

print(number_of_hits(3))

a, b, c, d, e = number_of_hits(1), number_of_hits(3), number_of_hits(5), number_of_hits(7), number_of_hits(1,2)

print(a,b,c,d,e)
print(a*b*c*d*e)

# ".#.#....##.......#..........#.."