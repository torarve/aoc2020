def read_input():
    with open("input5.txt") as file:
        return [x.strip() for x in file.readlines()]

def to_bin(seat):
    value = seat.replace("F", "0").replace("B", "1").replace("R", "1").replace("L", "0")
    return int(value, 2)

# print(to_bin("BFFFBBFRRR"))


seats = list([to_bin(x) for x in read_input()])
highest = max(seats)
lowest = min(seats)
print(highest)

for i in range(lowest, highest):
    if i not in seats:
        print(i)

#for x in sorted(seats):
#    print(x)

# print(653 in seats)