import numpy as np
f = np.array([int(n) for n in open('input','r')])
f.sort()
f = np.concatenate(([0],f,[f.max()+3]))
diff = f[1:]-f[:-1]
print((diff==1).sum()*(diff==3).sum())
