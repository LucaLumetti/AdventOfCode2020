import re
import itertools
f = open('input').readlines()

def msk(mask, value):
    bin_mask = mask.rstrip()
    bin_value = "{:036b}".format(int(value))
    return ''.join([ ('1' if bm == '1' else bv) if bm != 'X' else 'X' for bm,bv in zip(bin_mask, bin_value) ])

def get_all_memory_addr(s):
    x = s.count('X')
    comb = [list(i) for i in itertools.product(['0', '1'], repeat=x)]
    addrs = []
    for v in comb:
        sn = s
        for c in v:
            sn = sn.replace('X',c,1)
        addrs.append(sn)
    return addrs

mask = 'X'*36
memory = {}
for l in f:
    if(l[:4] == 'mask'):
        mask = l[7:].strip()
        continue
    rgx = re.search(r"mem\[(\d+)\] = (\d+)", l)
    addr = rgx[1]
    value = int(rgx[2])
    addrs = get_all_memory_addr(msk(mask, addr))
    for addr in addrs:
        memory[addr] = value

t = 0
for k in memory.keys():
    t += memory[k]
print(t)
