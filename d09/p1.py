import numpy as np
f = [ int(n) for n in open('input', 'r').readlines() ]
size = 25
n = -1

for i in range(size,len(f)):
    n = f[i]
    v = np.array(f[i-size:i])
    m = v[:,None] + v[None,:]
    np.fill_diagonal(m,0)
    if not n in m: break

print(n)
