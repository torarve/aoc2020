from collections import defaultdict

def get_input():
    with open('input24.txt') as file:
        return [x.strip() for x in file]

def parse_line(line):
    while len(line)>0:
        if line.startswith("w"):
            yield complex(-2, 0)
        elif line.startswith("e"):
            yield complex(2, 0)
        elif line.startswith("se"):
            yield complex(1, -1)
        elif line.startswith("sw"):
            yield complex(-1, -1)
        elif line.startswith("ne"):
            yield complex(1, 1)
        elif line.startswith("nw"):
            yield complex(-1, 1)
        
        if line.startswith("s") or line.startswith("n"):
            line = line[2:]
        else:
            line = line[1:]

def neighbours(point):
    return [point+x for x in [
        complex(-2, 0), complex(2, 0), complex(1, -1), 
        complex(-1, -1), complex(-1, 1), complex(1, 1)]]

def flip(flipped):
    counts = defaultdict(int)
    for point in flipped:
        for neighbour in neighbours(point):
            counts[neighbour] = counts[neighbour] + 1

    tmp = set(flipped)
    for point in flipped:
        if counts[point] == 0 or counts[point] > 2:
            tmp.remove(point)
    for point in counts:
        if point not in flipped and counts[point]==2:
            tmp.add(point)
    return tmp

# Test input
input = [
    "sesenwnenenewseeswwswswwnenewsewsw", 
    "neeenesenwnwwswnenewnwwsewnenwseswesw", 
    "seswneswswsenwwnwse", 
    "nwnwneseeswswnenewneswwnewseswneseene", 
    "swweswneswnenwsewnwneneseenw", 
    "eesenwseswswnenwswnwnwsewwnwsene", 
    "sewnenenenesenwsewnenwwwse", 
    "wenwwweseeeweswwwnwwe", 
    "wsweesenenewnwwnwsenewsenwwsesesenwne", 
    "neeswseenwwswnwswswnw", 
    "nenwswwsewswnenenewsenwsenwnesesenew", 
    "enewnwewneswsewnwswenweswnenwsenwsw", 
    "sweneswneswneneenwnewenewwneswswnese", 
    "swwesenesewenwneswnwwneseswwne", 
    "enesenwswwswneneswsenwnewswseenwsese", 
    "wnwnesenesenenwwnenwsewesewsesesew", 
    "nenewswnwewswnenesenwnesewesw", 
    "eneswnwswnwsenenwnwnwwseeswneewsenese", 
    "neswnwewnwnwseenwseesewsenwsweewe", 
    "wseweeenwnesenwwwswnew", 
]

input = get_input()
flipped = set()
for line in input:
    point = sum(parse_line(line))
    if point in flipped:
        flipped.remove(point)
    else:
        flipped.add(point)

print(f"There are {len(flipped)} flipped tiles initially.")

for i in range(0, 100):
    flipped = flip(flipped)

print(f"After 100 days there are {len(flipped)} flipped tiles.")