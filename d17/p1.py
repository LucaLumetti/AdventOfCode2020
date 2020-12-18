import math
import numpy as np
f = np.array([ [1 if c == '#' else 0 for c in l.rstrip()] for l in open('input').readlines() ])
steps = 6
dim = f.shape
l = int(math.floor(dim[0]/2))
u = int(math.floor(dim[1]/2))

space_dim = len(f[0]) + steps*2 -2
half_space_dim = int(math.floor(space_dim/2))
space = np.zeros((space_dim,space_dim,space_dim))

for i in range(dim[0]):
    for j in range(dim[1]):
        space[half_space_dim,half_space_dim-l+i,half_space_dim-u+j] = f[i][j]

def step(array, x,y,z):
    sx, sy, sz = x-1,y-1,z-1
    ex, ey, ez = x+1,y+1,z+1

    if(x == 0): sx = 0
    if(y == 0): sy = 0
    if(z == 0): sz = 0

    if(x == array.shape[0]-1): ex = x
    if(y == array.shape[1]-1): ey = y
    if(z == array.shape[2]-1): ez = z

    t = array[sx:ex+1, sy:ey+1, sz:ez+1].sum()
    if(array[x,y,z] == 1 and t in [3,4]): return True
    if(array[x,y,z] == 0 and t == 3): return True
    return False

spc = [space, space.copy()]

for k in range(steps):
    lower_bound = max(0,half_space_dim-l-k)
    upper_bound = min(space.shape[0],half_space_dim+l+k)
    for x in range(lower_bound, upper_bound):
        for y in range(lower_bound, upper_bound):
            for z in range(lower_bound, upper_bound):
                spc[k%2][x,y,z] = int(step(spc[(k+1)%2], x,y,z))

print(spc[1].sum())
