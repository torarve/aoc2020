import re

class Ship():
    def __init__(self):
        self.direction = 90
        self.x = 0
        self.y = 0

    @property
    def facing(self):
        i = int((self.direction % 360)/90)
        return ["N", "E", "S", "W"][i]
    
    def do(self, command):
        action, value = re.fullmatch("(N|S|E|W|L|R|F)(\\d+)", command).groups()
        value = int(value)
        self._handle(action, value)

    def _handle(self, action, value):
        if action == "N":
            self.y += value
        elif action == "S":
            self.y -= value
        elif action == "E":
            self.x += value
        elif action == "W":
            self.x -= value
        elif action == "L":
            self.direction -= value
        elif action == "R":
            self.direction += value
        elif action == "F":
            self._handle(self.facing, value)

s = Ship()
with open('input12.txt') as file:
    for line in file:
        if line!="":
            s.do(line.strip())

print(f"Manhatten distance: {abs(s.x)+abs(s.y)}")

class Ship2():

    def __init__(self):
        self.waypoint_x = 10
        self.waypoint_y = 1
        self.x = 0
        self.y = 0
  
    def do(self, command):
        action, value = re.fullmatch("(N|S|E|W|L|R|F)(\\d+)", command).groups()
        value = int(value)
        self._handle(action, value)

    def _handle(self, action, value):
        if action == "N":
            self.waypoint_y += value
        elif action == "S":
            self.waypoint_y -= value
        elif action == "E":
            self.waypoint_x += value
        elif action == "W":
            self.waypoint_x -= value
        elif action == "L":
            self.rotate_waypoint(-value)
        elif action == "R":
            self.rotate_waypoint(value)
        elif action == "F":
            self.y += self.waypoint_y*value
            self.x += self.waypoint_x*value

    def rotate_waypoint(self, value):
        value = value % 360
        if value == 90:
            self.waypoint_x, self.waypoint_y = self.waypoint_y, -self.waypoint_x
        elif value == 180:
            self.waypoint_x, self.waypoint_y = -self.waypoint_x, -self.waypoint_y
        elif value == 270:
            self.waypoint_x, self.waypoint_y = -self.waypoint_y, self.waypoint_x

s = Ship2()
with open('input12.txt') as file:
    for line in file:
        if line!="":
            s.do(line.strip())

print(f"Manhatten distance: {abs(s.x)+abs(s.y)}")
