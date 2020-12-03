f = [ s.strip() for s in open('input', 'r').readlines() ]
total = 1
for d in [[1,1],[3,1],[5,1],[7,1],[1,2]]:
    trees = 0
    pos = [0, 0]
    while pos[1] < len(f)-1:
        pos[0] += d[0]
        pos[0] %= len(f[0])
        pos[1] += d[1]
        trees += f[pos[1]][pos[0]] == '#'
    total *= trees
print(total)
