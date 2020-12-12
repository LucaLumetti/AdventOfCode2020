import numpy as np
import time
f = open('input','r').read()
dim = (len(f.strip().split('\n')),len(f.split('\n')[0].strip()))

f = np.array(list(f.replace('\n',''))).reshape(dim)

f_new = f.copy()
changes = True
while changes:
    changes = False
    timer = time.time()
    for x,y in np.argwhere(f!='.'):
        t = f[x, y-1] if y > 0 else '.'
        tl = f[x-1, y-1] if y > 0 and x > 0 else '.'
        tr = f[x+1, y-1] if y > 0 and x < dim[0]-1 else '.'
        r = f[x+1, y] if x < dim[0]-1 else '.'
        l = f[x-1, y] if x > 0 else '.'
        b = f[x, y+1] if y < dim[1]-1 else '.'
        bl = f[x-1, y+1] if y < dim[1]-1 and x > 0 else '.'
        br = f[x+1, y+1] if y < dim[1]-1 and x < dim[0]-1 else '.'
        if not '#' in [t,tl,tr,r,l,b,bl,br] and f[x,y] == 'L':
            changes = True
            f_new[x,y] = '#'

        if (np.array([t,tl,tr,r,l,b,bl,br])=='#').sum()>=4 and f[x,y] == '#':
            changes = True
            f_new[x,y] = 'L'
    f = f_new.copy()
print((f_new == '#').sum())
