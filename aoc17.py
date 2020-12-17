import re

def get_input():
    with open('input17.txt') as file:
        return [x.strip() for x in file]

# #####
# ..#..
# #..#.
# #####
# ..#..

class Cube:
    def __init__(self, size, dimensions=3):
        self.size = size
        self.dimensions = dimensions
        self.values = [0]*pow(size, dimensions)

    @property
    def plane_size(self):
        return self.size*self.size

    def add(self, values, index=0):
        tmp = [x+y for x,y in zip(self.values[index:], values)]
        self.values[index:len(tmp)] = tmp

    def __repr__(self):
        result = []
        for i in range(0, self.size):
            plane = self.values[i*self.plane_size:(i+1)*self.plane_size]
            tmp = []
            for j in range(0, self.size):
                tmp.append(" ".join([f"{x:4}" for x in plane[j*self.size:(j+1)*self.size]]))

            result.append(f"Plane {i}\n" + "\n".join(tmp))
        return "\n\n".join(result)
        
class Space:
    def __init__(self, size, dimensions=3):
        self.cube = Cube(size, dimensions)

    def count3d(self):
        counts = Cube(self.cube.size)
        plane_size = self.cube.plane_size
        size = self.cube.size

        for z in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                for x in [-1, 0, 1]:
                    offset = z*plane_size + y*size + x
                    if offset<0:
                        counts.add(self.cube.values, -offset)
                    elif offset>0:
                        counts.add(self.cube.values[offset:])
        return counts

    def count4d(self):
        counts = Cube(self.cube.size, self.dimensions)
        plane_size = self.cube.plane_size
        size = self.cube.size

        for w in [-1, 0, 1]:
            for z in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    for x in [-1, 0, 1]:
                        offset = w*size*plane_size + z*plane_size + y*size + x
                        if offset<0:
                            counts.add(self.cube.values, -offset)
                        elif offset>0:
                            counts.add(self.cube.values[offset:])
        return counts

    @property
    def dimensions(self):
        return self.cube.dimensions

    def run_cycle(self):
        if self.dimensions == 3:
            counts = self.count3d()
        elif self.dimensions == 4:
            counts = self.count4d()
        else:
            raise "Invalid dimension"

        def new_state(old, count):
            if count==3:
                return 1
            elif old==1 and count==2:
                return 1
            
            return 0

        self.cube.values = [new_state(x, y) for x,y in zip(self.cube.values, counts.values)]

# cubes = []

# 3*3*3 = 27
initial_state = get_input()
# initial_state = [
#     ".#.",
#     "..#",
#     "###",
# ]
size = len(initial_state)+6*2 # = 3 + 6*2 = 15

print(f"size={size}")
mid = size//2
offset = len(initial_state)//2
print(f"offset={offset}")
print(f"mid={mid}")

space = Space(size)
for y, line in enumerate(initial_state):
    for x, char in enumerate(line):
        if char=='#':
            space.cube.values[mid*size*size + (y+mid-offset) * size + x + mid-offset] = 1

space.run_cycle()
space.run_cycle()
space.run_cycle()
space.run_cycle()
space.run_cycle()
space.run_cycle()
print(space.cube.values.count(1))

space = Space(size, 4)
for y, line in enumerate(initial_state):
    for x, char in enumerate(line):
        if char=='#':
            space.cube.values[mid*size*size*size + mid*size*size + (y+mid-offset) * size + x + mid-offset] = 1

space.run_cycle()
space.run_cycle()
space.run_cycle()
space.run_cycle()
space.run_cycle()
space.run_cycle()
print(space.cube.values.count(1))
