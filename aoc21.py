import re

def get_input():
    with open('input21.txt') as file:
        return [x.strip() for x in file]

input = [
    "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
    "trh fvjkl sbzzf mxmxvkd (contains dairy)",
    "sqjhc fvjkl (contains soy)",
    "sqjhc mxmxvkd sbzzf (contains fish)",
]

input = get_input()
all_allergens = set()
all_ingredients = set()

lines = []
for line in input:
    m = re.fullmatch("(.*) \\(contains (.*)\\)", line)
    if m is None:
        print(f"Unable to parse '{line}'")
        exit()

    part1, part2 = m.groups()
    ingredients = part1.split(" ")
    for i in ingredients:
        all_ingredients.add(i)
    allergens = part2.split(", ")
    for a in all_allergens:
        all_allergens.add(a)
    lines.append((ingredients, allergens))

possibilities = {}
for ingredients, allergens in lines:
    for allergen in allergens:
        if allergen in possibilities.keys():
            possibilities[allergen].intersection_update(ingredients)
        else:
            possibilities[allergen] = set(ingredients)

unknown_ingredients = set(all_ingredients)
for s in possibilities.values():
    unknown_ingredients.difference_update(s)

count = 0
for ingredients, allergens in lines:
    count += sum([ingredients.count(x) for x in unknown_ingredients])

print(f"Number of ingredients that can't be any allergen: {count}")

result = {}
while True:
    found = [x for x,y in possibilities.items() if len(y)==1]
    if len(found)==0:
        break

    tmp = []
    for f in found:
        i = possibilities[f].pop()
        result[f] = i
        tmp.append(i)
        del possibilities[f]

    for p in possibilities:
        possibilities[p].difference_update(tmp)

canonical_ingredient_list = ",".join([y for x,y in sorted([(x,y) for x, y in result.items()], key = lambda pair: pair[0])])
print(f"Canonical ingredient list: {canonical_ingredient_list}")
