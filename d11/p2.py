import numpy as np
f = open('input','r').read()
dim = (len(f.strip().split('\n')),len(f.split('\n')[0].strip()))

f = np.array(list(f.replace('\n',''))).reshape(dim)

def find_dir(arr, dirs, start):
    pos = start
    pos[0] += dirs[0]
    pos[1] += dirs[1]
    while 0 <= pos[0] < dim[0] and 0 <= pos[1] < dim[1]:
        if(arr[pos[0]][pos[1]] != '.'): return arr[pos[0]][pos[1]]
        pos[0] += dirs[0]
        pos[1] += dirs[1]
    return '.'


f_new = f.copy()
changes = True
while changes:
    changes = False
    for x,y in np.argwhere(f!='.'):
        t = find_dir(f, (0,1), [x,y])
        tl = find_dir(f, (-1,1), [x,y])
        tr = find_dir(f, (1,1), [x,y])
        r = find_dir(f, (1,0), [x,y])
        l = find_dir(f, (-1,0), [x,y])
        b = find_dir(f, (0,-1), [x,y])
        bl = find_dir(f, (-1,-1), [x,y])
        br = find_dir(f, (1,-1), [x,y])
        if not '#' in [t,tl,tr,r,l,b,bl,br] and f[x,y] == 'L':
            changes = True
            f_new[x,y] = '#'

        if (np.array([t,tl,tr,r,l,b,bl,br])=='#').sum()>=5 and f[x,y] == '#':
            changes = True
            f_new[x,y] = 'L'
    f = f_new.copy()
print((f_new == '#').sum())
