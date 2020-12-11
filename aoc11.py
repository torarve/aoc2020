import re

def get_input():
    with open('input11.txt') as file:
        return [x.strip() for x in file if x.strip()!=""]

class Map:
    def __init__(self, layout):
        self.layout = layout
    
    def get(self, x, y):
        if y<0 or y>=len(self.layout):
            return "."
        tmp = self.layout[y]
        if x<0 or x>=len(tmp):
            return "."
        return tmp[x]

    def get_adjacent(self, x, y):
        return [
            self.get(x-1, y-1), self.get(x, y-1), self.get(x+1, y-1),
            self.get(x-1, y), self.get(x+1, y),
            self.get(x-1, y+1), self.get(x, y+1), self.get(x+1, y+1),
        ]

    def occupied_seats_adjacent(self, x,y):
        return len([x for x in self.get_adjacent(x, y) if x=="#"])
    
    def do_round(self):
        result = []
        counter = 0
        for y, row in enumerate(self.layout):
            tmp = ""
            for x, seat in enumerate(row):
                num_occupied_seats = self.occupied_seats_adjacent(x,y)
                if seat=="L" and num_occupied_seats==0:
                    tmp += "#"
                    counter += 1
                elif seat=="#" and num_occupied_seats>=4:
                    tmp += "L"
                    counter += 1
                else:
                    tmp += seat
            result.append(tmp)
        self.layout = result
        return counter

    def get_stable_count(self):
        count = 0
        while self.do_round()>0:
            count += 1
        return count

    def occupied_seat_count(self):
        return sum([x.count("#") for x in self.layout])


class Map2:
    def __init__(self, layout):
        self.layout = layout
    
    def get(self, x, y):
        if y<0 or y>=len(self.layout):
            return None
        tmp = self.layout[y]
        if x<0 or x>=len(tmp):
            return None
        return tmp[x]

    def get_in_direction(self, x, y, step_x, step_y):
        print(f"get_in_direction({x},{y},{step_x},{step_y})")
        x += step_x
        y += step_y
        seat = self.get(x,y)
        while seat is not None:
            if seat!=".":
                break
            x += step_x
            y += step_y
            seat = self.get(x,y)
                
        return seat

    def get_left(self, x, y):
        if y<0 or y>=len(self.layout):
            return None
        row = self.layout[y]
        if x<1 or x>=len(row):
            return None
        row = row[:x-1]
        tmp = [x for x in reversed(row) if x!="."]
        if len(tmp)==0:
            return None
        return tmp[0]

    def get_right(self, x, y):
        if y<0 or y>=len(self.layout):
            return None
        row = self.layout[y]
        if x<0 or x>=len(row)-1:
            return None
        row = row[:x+1]
        return [x for x in row if x!="."][0]

    def get_adjacent(self, x, y):
        return [
            self.get_in_direction(x, y, -1, -1), self.get_in_direction(x, y, 0, -1), self.get_in_direction(x, y, 1, -1),
            # self.get_left(x,y), self.get_right(x,y),
            self.get_in_direction(x, y, -1, 0), self.get_in_direction(x, y, 1, 0),
            self.get_in_direction(x, y, -1, 1), self.get_in_direction(x, y, 0, 1), self.get_in_direction(x, y, 1, 1),
        ]

    def occupied_seats_adjacent(self, x,y):
        return len([x for x in self.get_adjacent(x, y) if x=="#"])
    
    def do_round(self):
        result = []
        counter = 0
        for y, row in enumerate(self.layout):
            tmp = ""
            for x, seat in enumerate(row):
                num_occupied_seats = self.occupied_seats_adjacent(x,y)
                if seat=="L" and num_occupied_seats==0:
                    tmp += "#"
                    counter += 1
                elif seat=="#" and num_occupied_seats>=5:
                    tmp += "L"
                    counter += 1
                else:
                    tmp += seat
            result.append(tmp)
        self.layout = result
        return counter

    def get_stable_count(self):
        count = 0
        while self.do_round()>0:
            count += 1
        return count

    def occupied_seat_count(self):
        return sum([x.count("#") for x in self.layout])

test = [
    "L.LL.LL.LL",
    "LLLLLLL.LL",
    "L.L.L..L..",
    "LLLL.LL.LL",
    "L.LL.LL.LL",
    "L.LLLLL.LL",
    "..L.L.....",
    "LLLLLLLLLL",
    "L.LLLLLL.L",   
    "L.LLLLL.LL"
]

# m = Map(get_input())
m = Map(test)
m.get_stable_count()
print(m.occupied_seat_count())

# m = Map2(test)
m = Map2(get_input())
m.get_stable_count()
print(m.layout)
print(m.occupied_seat_count())
