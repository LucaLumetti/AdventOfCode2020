import math
import numpy as np
f = open('input').readlines()
t = int(f[0])
bus = [int(n) for n in f[1].split(',') if n != 'x']
fbus = [t/b for b in bus]
rbus = np.array([math.ceil(b)-b for b in fbus])
minbus = np.argmin(rbus)
print(bus[minbus]**2 * math.ceil(fbus[minbus]) - t*bus[minbus])
