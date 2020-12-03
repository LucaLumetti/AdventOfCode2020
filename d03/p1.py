f = [ s.strip() for s in open('input', 'r').readlines() ]
trees = 0
pos = [0, 0]
while pos[1] < len(f)-1:
    pos[0] += 3
    pos[0] %= len(f[0])
    pos[1] += 1
    trees += f[pos[1]][pos[0]] == '#'
print(trees)
