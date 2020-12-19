import itertools

def read_input():
    with open("input1.txt") as file:
        return [int(x.strip()) for x in file.readlines() if x != ""]

numbers = read_input()

i, j = [tuple(x) 
    for x in itertools.combinations(numbers, 2) 
    if sum(x)==2020].pop()

print(f"{i}+{j}=2020, {i}*{j}={i*j}")

i, j, k = [tuple(x)
    for x in itertools.combinations(numbers, 3)
    if sum(x)==2020].pop()
print(f"{i}+{j}+{k}=2020, {i}*{j}*{k}={i*j*k}")
