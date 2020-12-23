from collections import deque

def solve4(cups, rounds):
    high = max(cups)
    size = len(cups)
    q = deque(cups)
    for i in range(0, rounds):
        current = q.popleft()
        pick = [q.popleft(), q.popleft(), q.popleft()]
        to_find = 1 + (current - 2) % high
        while to_find in pick:
            to_find = 1 + (to_find - 2) % high

        idx = q.index(to_find)
        q.rotate(size-idx-5)
        q.extend(pick)
        q.rotate(-size+idx+5)
        q.append(current)
    return list(q)

def solve5(initial, size, rounds):
    # Everthing points to next
    indices = [(x+1)%size for x in range(0,size)]
    for i in range(0, len(initial)-1):
        indices[initial[i]-1] = initial[(i+1)]-1
    indices[initial[-1]-1] = len(initial)
    indices[-1] = initial[0]-1

    current = initial[0]-1
    for i in range(0, rounds):
        first = indices[current]
        second = indices[first]
        third = indices[second]
        
        to_find = (current-1) % size
        while to_find in [first, second, third]:
            to_find = (to_find-1) % size

        indices[current] = indices[third]
        indices[third] = indices[to_find]
        indices[to_find] = first

        current = indices[current]

    first = indices[0]
    second = indices[first]
    return (first+1, second+1)

input = "389125467"
input = "135468729"

cups = [int(x) for x in input]
size = len(cups)

cups = solve4(cups, 100)
start = cups.index(1)
print("".join([str(cups[(start+i)%size]) for i in range(1,size)]))
print()

input = "389125467"
input = "135468729"

cups = [int(x) for x in input]
first, second = solve5(cups, 1000000, 10000000)
print(first*second)
