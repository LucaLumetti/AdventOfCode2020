import re
from collections import Counter
f = open('input').readlines()

rg = re.compile('[ns]?[ew]')
dirs = {
        'e':  +1+0j,
        'ne': +1-1j,
        'nw': +0-1j,
        'w':  -1+0j,
        'sw': -1+1j,
        'se': +0+1j,
        }

changes = Counter(sum(dirs[m[0]] for m in rg.finditer(l)) for l in f)
blacks = {k for k, v in changes.items() if v%2}

print(len(blacks))

for k in range(100):
    neigh = Counter(pt+d for pt in blacks for d in dirs.values())
    new_blacks = set()
    for k,v in neigh.items():
        if k not in blacks and v == 2:
            new_blacks |= {k}
        if k in blacks and (v == 1 or v == 2):
            new_blacks |= {k}
    blacks = new_blacks

print(len(blacks))
