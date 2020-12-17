import re
import numpy as np
f = open('input').readlines()

nti = None
yti = None
for i,l in enumerate(f):
    if 'your' in l:
        yti = i+1
        continue
    if 'nearby' in l:
        nti = i+1
        break

classes = re.finditer(r"[a-zA-Z\ ]+:\ (\d+-\d+) or (\d+-\d+)", '\n'.join(f))
classes = [ c[1].split('-')+c[2].split('-') for c in classes ]
# print(nti)
nearby_tickets = np.array([ np.array([int(n) for n in l.rstrip().split(',')]) for l in f[nti:]])
your_ticket = f[yti].rstrip()
# print(your_ticket)
for c in classes:
    a = np.logical_and(nearby_tickets >= int(c[0]), nearby_tickets <= int(c[1]))
    b = np.logical_and(nearby_tickets >= int(c[2]), nearby_tickets <= int(c[3]))
    nearby_tickets = nearby_tickets[np.logical_not(np.logical_or(a,b))]
print(nearby_tickets.sum())
