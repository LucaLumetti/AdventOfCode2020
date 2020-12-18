f = [int(n) for n in open('input').read().rstrip().split(',')]
said_num = {}

for i,n in enumerate(f[:-1]):
    said_num[n] = i

to_say = f[-1]
for i in range(len(f)-1, 30000000-1):
    if(not to_say in said_num.keys()):
        next_num = 0
    else:
        next_num = i - said_num[to_say]
    said_num[to_say] = i
    to_say = next_num
print(to_say)
