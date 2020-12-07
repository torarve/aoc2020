def get_input():
    with open('input6.txt') as file:
        return [x.strip() for x in file]

def get_answers1():
    lines = get_input()
    if lines[-1] != "":
        lines.append("")
    result = set()
    for line in lines:
        if line == "":
            yield result
            result = set()
        else:
            for c in line: result.add(c)

answers = get_answers1()
counts = [len(x) for x in answers]
print(sum(counts))


def get_answers2():
    lines = get_input()
    if lines[-1] != "":
        lines.append("")
    result = None
    for line in lines:
        if line == "":
            yield result
            result = None
        else:
            if result is None:
                result = set(line)
            else:
                result = result.intersection(set(line))


answers2 = get_answers2()
counts2 = [len(x) for x in answers2]
print(sum(counts2))
