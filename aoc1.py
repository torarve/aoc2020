numbers = []

with open("input1.txt") as file:
    numbers = [int(x.strip()) for x in file.readlines() if x != ""]

for i in numbers:
    for j in numbers:
        if i + j == 2020:
            # print(i, j)
            print(i*j)

for i in numbers:
    for j in numbers:
        for k in numbers:
            if i + j + k == 2020:
                # print(i, j, k)
                print(i*j*k)
