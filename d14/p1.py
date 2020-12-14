import re
f = open('input').readlines()

def msk(mask, value):
    bin_mask = mask.rstrip()
    bin_value = "{:036b}".format(int(value))
    return int("0b" + ''.join([ bm if bm != 'X' else bv for bm,bv in zip(bin_mask, bin_value) ]), 2)

mask = 'X'*36
memory = {}
for l in f:
    if(l[:4] == 'mask'):
        mask = l[7:].strip()
        continue
    rgx = re.search(r"mem\[(\d+)\] = (\d+)",l)
    addr = rgx[1]
    value = rgx[2]
    memory[addr] = msk(mask, value)

total = 0
for k in memory.keys():
    total += memory[k]
print(total)
