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

classes = list(re.finditer(r"([a-zA-Z\ ]+):\ (\d+-\d+) or (\d+-\d+)", '\n'.join(f)))
classes_name = [ c[1] for c in classes ]
classes = [ [c[2],c[3]] for c in classes ]
classes = [ [int(n) for n in c[0].split('-')]+[int(n) for n in c[1].split('-')] for c in classes ]
# print(nti)
nearby_tickets = np.array([ np.array([int(n) for n in l.rstrip().split(',')]) for l in f[nti:]])
your_ticket = [int(n) for n in f[yti].rstrip().split(',')]

def check_ticket(ticket, classes):
    valid = False
    for v in ticket:
        for c in classes:
            if(c[0] <= v <= c[1] or c[2] <= v <= c[3]):
                valid = True
                break
        if(valid):
            valid = False
            continue
        else:
            return False
    return True

def find_class(ticket, classes):
    valid_classes = []
    for ic,c in enumerate(classes):
        valid = True
        for t in ticket:
            if(not(c[0] <= t <= c[1] or c[2] <= t <= c[3])):
                valid = False
                break
        if(valid): valid_classes.append(ic)
    return valid_classes

nearby_tickets = np.array([ ticket for ticket in nearby_tickets if check_ticket(ticket, classes) ])

valid_class_for_row = np.array([ find_class(r, classes) for r in nearby_tickets.T ], dtype="object")

used_classes = []
def all_len_one(a):
    return sum([len(i) for i in a]) == len(a)

def remove_used(a,b):
    new_a = []
    for e in a:
        if not e in b:
            new_a.append(e)
    return new_a

while not all_len_one(valid_class_for_row):
    for i,row in enumerate(valid_class_for_row):
        if(len(row) == 1):
            if(row[0] not in used_classes): used_classes.append(row[0])
            continue
        valid_class_for_row[i] = remove_used(valid_class_for_row[i], used_classes)

used_classes = np.array([ e[0] for e in valid_class_for_row])

print(np.array(your_ticket)[used_classes < 6].prod())
