import numpy as np
f = np.array([int(n) for n in open('test','r')])
f.sort()
f = np.concatenate(([0],f,[f.max()+3]))
diff = list(f[1:]-f[:-1])

ones = []
for x in range(len(diff)):
    if(x != 0 and diff[x-1] == 1):
        ones.append(0)
        continue
    for n in range(len(diff)):
        if(diff[x:x+n] == [1]*n and diff[x:x+n+1] != [1]*(n+1)):
            ones.append(n)
            break
d = {0:1,1:1,2:2,3:4,4:7,5:13} # can this be improv?
print(np.array([d[x] for x in ones]).prod())
