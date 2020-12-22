import numpy as np
f = open('input').readlines()

total_allergens = set()
total_ingredients = set()

for l in f:
    l = l.rstrip()
    spl = l.split(' (contains ')
    ingredients = spl[0].split(' ')
    allergens = spl[1][:-1].split(', ')
    total_allergens = total_allergens.union(set(allergens))
    total_ingredients = total_ingredients.union(set(ingredients))

allergens_ingredients = {}
for l in f:
    l = l.rstrip()
    spl = l.split(' (contains ')
    ingredients = spl[0].split(' ')
    allergens = spl[1][:-1].split(', ')
    for aller in allergens:
        if(not aller in allergens_ingredients):
            allergens_ingredients[aller] = set(total_ingredients)
        allergens_ingredients[aller] = allergens_ingredients[aller].intersection(set(ingredients))

found_ingredients = set()
solution = {}
for _,_ in allergens_ingredients.items():
    for k,v in allergens_ingredients.items():
        v = v-found_ingredients
        if(len(v) == 1):
            found_ingredients = found_ingredients.union(v)
            solution[k] = v

free_ingredients = set()
p2sol_allergens = []
p2sol_ingredients = []
for k,v in solution.items():
    free_ingredients = free_ingredients.union(v)
    p2sol_ingredients.append(v.pop())
    p2sol_allergens.append(k)

p2sol_ingredients = np.array(p2sol_ingredients)
p2sol_allergens = np.array(p2sol_allergens)
free_ingredients = total_ingredients - free_ingredients

count = 0
for l in f:
    l = l.rstrip()
    spl = l.split(' (contains ')
    ingredients = set(spl[0].split(' '))
    for i in ingredients:
        count += i in free_ingredients
print(count)
print(','.join(p2sol_ingredients[np.argsort(p2sol_allergens)]))
