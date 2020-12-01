import numpy as np
f = open('input', 'r')
f = np.array([ int(n) for n in f.readlines() ])

tot2 = f[:,None] + f[None,:]
print(f[np.argwhere(tot2 == 2020)[0]].prod())

tot3 = tot2[:,:,None] + f[None,:]
print(f[np.argwhere(tot3 == 2020)[0]].prod())
