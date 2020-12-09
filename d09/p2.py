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

start = 0
end = 1
while(end < len(f)):
    s = sum(f[start:end])
    start += s > n
    end += s < n
    if(s == n): break

print(max(f[start:end])+min(f[start:end]))
