import re
parent = r"^(\w+\ \w+) bags contain"
childrens = r"(\d+) (\w+ \w+) bags?"
f = open('input', 'r').readlines()

p = [ re.findall(parent, l)[0] for l in f ]
cn = [ [ g[1] for g in re.findall(childrens, l) if len(g) == 2 ] for l in f ]
cc = [ [ int(g[0]) for g in re.findall(childrens, l) if len(g) == 2 ] for l in f ]
empty_bags = [ p[i] for i,b in enumerate(cc) if len(b) == 0] # just to speed up

pointers = ["shiny gold"]
total = 0

for pt in pointers:
    if pt in empty_bags: continue # just to speed up
    for i,b in enumerate(cn):
        if(p[i] != pt): continue
        print(b)
        for cx,bx in zip(cc[i],b):
            pointers.extend([bx]*cx)
            total += cx
print(total)

