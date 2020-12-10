import re
import functools

def get_input():
    with open('input10.txt') as file:
        return [int(x.strip()) for x in file if x.strip()!=""]

lines = [0]
lines.extend(get_input())
lines.sort()
lines.append(lines[-1]+3)

def find_differences(lines):
    return list(map(lambda x, y: x-y, lines[1:], lines[:-1]))

def count_differences(lines):
    diff = find_differences(lines)
    return diff.count(1), diff.count(3)

a, b = count_differences(lines)
print(a*b)

def is_valid(lines):
    diffs = set(find_differences(lines))
    return len(diffs)>0 and (min(diffs)>0 and min(diffs)<=3)

cache = {}

def count_valid_arrangements(lines):
    key = str(lines)
    if key in cache.keys():
        return cache[key]

    tmp = lines[:]
    if len(tmp)<3:
        cache[key] = 1
        return 1
        
    if not is_valid(lines):
        cache[key] = 0
        return 0

    count = count_valid_arrangements(tmp[:-1])
    if len(tmp)>3 and (tmp[-1]-tmp[-4]<=3):
        count += count_valid_arrangements(tmp[:-3]) + count_valid_arrangements(tmp[:-2])
    elif len(tmp)>2 and (tmp[-1]-tmp[-3]<=3):
        count += count_valid_arrangements(tmp[:-2])
        
    cache[key] = count
    return count

tmp = [0]
tmp.extend([28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3])
tmp.sort()
tmp.append(tmp[-1]+3)

print(count_valid_arrangements(lines))