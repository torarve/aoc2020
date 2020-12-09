import re

def get_input():
    with open('input9.txt') as file:
        return [int(x.strip()) for x in file]

preamble_length = 25

def is_sum_of_two(number, numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                if number==(numbers[i] + numbers[j]):
                    return False
    return True

numbers = get_input()

def find_part1():
    current = []
    for number in numbers:
        if len(current)>=preamble_length:
            if is_sum_of_two(number, current):
                return number
            current.append(number)
            current = current[1:]
        else:
            current.append(number)        

part1 = find_part1()
print(part1)

def find_part2(answer):
    current = []
    for number in numbers:
        current.append(number)
        result = sum(current)
        while result > answer:
            current = current[1:]
            result = sum(current)
        if result==answer:
            return current

part2 = find_part2(part1)
print(min(part2)+max(part2))