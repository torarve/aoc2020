import re
import math

def get_input():
    with open('input20.txt') as file:
        return [x.strip() for x in file]

class Tile:
    def __init__(self, data):
        self.size = len(data)
        self._data = "".join(data)

    def __repr__(self):
        return "\n".join(self.rows)

    @property
    def top(self):
        return self._data[0:self.size]

    @property
    def bottom(self):
        return self._data[self.size*(self.size-1):]

    @property
    def right(self):
        return self._data[self.size-1::self.size]

    @property
    def left(self):
        return self._data[0::self.size]

    @property
    def rows(self):
        return [self._data[y*self.size:(y+1)*self.size] for y in range(0,self.size)]

    def _row(self, y):
        return self._data[y*self.size:(y+1)*self.size]

    def flip_horizontal(self):
        return Tile([self._row(y) for y in range(self.size-1, -1, -1)])

    def rotate(self):
        result = Tile([self._data[(self.size-1)*self.size+i::-self.size] 
            for i in range(0, self.size)])
        return result

def parse_tiles(lines):
    current_tile = 0
    data = []
    for line in lines:
        if line=="":
            yield current_tile, Tile(data)
            current_tile = 0
            data = []
        else:
            m = re.fullmatch("Tile (\\d+):", line)
            if m is not None:
                id, = m.groups()
                current_tile = int(id)
            else:
                data.append(line)


lines = [
    "Tile 2311:",
    "..##.#..#.",
    "##..#.....",
    "#...##..#.",
    "####.#...#",
    "##.##.###.",
    "##...#.###",
    ".#.#.#..##",
    "..#....#..",
    "###...#.#.",
    "..###..###",
    "",
    "Tile 1951:",
    "#.##...##.",
    "#.####...#",
    ".....#..##",
    "#...######",
    ".##.#....#",
    ".###.#####",
    "###.##.##.",
    ".###....#.",
    "..#.#..#.#",
    "#...##.#..",
    "",
    "Tile 1171:",
    "####...##.",
    "#..##.#..#",
    "##.#..#.#.",
    ".###.####.",
    "..###.####",
    ".##....##.",
    ".#...####.",
    "#.##.####.",
    "####..#...",
    ".....##...",
    "",
    "Tile 1427:",
    "###.##.#..",
    ".#..#.##..",
    ".#.##.#..#",
    "#.#.#.##.#",
    "....#...##",
    "...##..##.",
    "...#.#####",
    ".#.####.#.",
    "..#..###.#",
    "..##.#..#.",
    "",
    "Tile 1489:",
    "##.#.#....",
    "..##...#..",
    ".##..##...",
    "..#...#...",
    "#####...#.",
    "#..#.#.#.#",
    "...#.#.#..",
    "##.#...##.",
    "..##.##.##",
    "###.##.#..",
    "",
    "Tile 2473:",
    "#....####.",
    "#..#.##...",
    "#.##..#...",
    "######.#.#",
    ".#...#.#.#",
    ".#########",
    ".###.#..#.",
    "########.#",
    "##...##.#.",
    "..###.#.#.",
    "",
    "Tile 2971:",
    "..#.#....#",
    "#...###...",
    "#.#.###...",
    "##.##..#..",
    ".#####..##",
    ".#..####.#",
    "#..#.#..#.",
    "..####.###",
    "..#.#.###.",
    "...#.#.#.#",
    "",
    "Tile 2729:",
    "...#.#.#.#",
    "####.#....",
    "..#.#.....",
    "....#..#.#",
    ".##..##.#.",
    ".#.####...",
    "####.#.#..",
    "##.####...",
    "##..#.##..",
    "#.##...##.",
    "",
    "Tile 3079:",
    "#.#.#####.",
    ".#..######",
    "..#.......",
    "######....",
    "####.#..#.",
    ".#...#.##.",
    "#.#####.##",
    "..#.###...",
    "..#.......",
    "..#.###...",
    ""
]

tiles = dict([x for x in parse_tiles(lines)])
tiles = dict([x for x in parse_tiles(get_input())])
size = int(math.sqrt(len(tiles)))
print(f"Number of tiles: {len(tiles)}")
print(f"Number of dimensions: {size}")

def rotations_and_reflections(tile: Tile):
    t = Tile(tile.rows)
    yield t
    t = t.rotate()
    yield t
    t = t.rotate()
    yield t
    t = t.rotate()
    yield t
    t = tile.flip_horizontal()
    yield t
    t = t.rotate()
    yield t
    t = t.rotate()
    yield t
    t = t.rotate()
    yield t

def find_solution_impl(solution, count, tiles):
    remaining = set(tiles.keys()).difference([x for x in solution if x is not None])
    x = count % size
    y = count // size
    right = bottom = None
    if x>0:
        right = tiles[solution[count-1]].right
    if y>0:
        bottom = tiles[solution[count-size]].bottom

    for t in remaining:
        solution[count] = t
        saved = tiles[t]
        for tile in rotations_and_reflections(tiles[t]):
            if x>0:
                if right!=tile.left:
                    continue
            if y>0:
                if bottom!=tile.top:
                    continue

            tiles[t] = tile
            if count<len(solution)-1:
                result = find_solution_impl(solution, count+1, tiles)
                if result is not None:
                    return result
            else:
                return solution

        tiles[t] = saved
        solution[count] = None

    return None

def find_solution(tiles):
    solution = [None]*(size*size)
    for t in tiles:
        print(f"Checking {t}...")
        solution[0] = t

        for tile in rotations_and_reflections(tiles[t]):
            tiles[t] = tile
            result = find_solution_impl(solution, 1, tiles)
            if result is not None:
                return result
        
result = find_solution(tiles)

print(result[0]*result[size-1]*result[size*(size-1)]*result[size*size-1])

monster = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]

image_data = []
for i in range(0,size):
    def clip_and_join(args):
        return "".join([x[1:-1] for x in args])

    row = [tiles[x].rows[1:-1] for x in result[i*size:(i+1)*size]]
    image_data.extend([clip_and_join (x) for x in zip(*list(row))])

m_width = len(monster[0])
m_height = len(monster)
width = len(image_data[0])
height = len(image_data)

def matches(line, filter):
    return all([b!="#" or a=="#" for a,b in zip(line, filter)])

def find_monsters(image_data, filter):
    for tile in rotations_and_reflections(Tile(image_data)):
        result = []
        for y in range(0, height-m_height+1):
            lines = tile.rows[y:(y+m_height)]
            for x in range(0,width-m_width+1):
                m = [matches(lines[i][x:x+m_width], filter[i]) for i in range(0, m_height)]
                if all(m):
                    result.append((x,y))
        if len(result)>0:
            return result

found_monsters = find_monsters(image_data, monster)
roughness = sum([row.count("#") for row in image_data])-len(found_monsters)*sum([row.count("#") for row in monster])
print(roughness)