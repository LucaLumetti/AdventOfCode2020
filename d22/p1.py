f = [ l.split('\n')[1:] for l in open('input').read().rstrip().split('\n\n') ]
f[0] = [ int(n) for n in f[0] ]
f[1] = [ int(n) for n in f[1] ]

def game_round(p1, p2):
    a = p1[0]
    b = p2[0]
    p1 = p1[1:]
    p2 = p2[1:]
    if(a > b):
        p1.extend([a,b])
    else:
        p2.extend([b,a])
    return p1,p2

while(len(f[0]) != 0 and len(f[1]) != 0):
    f[0],f[1] = game_round(f[0],f[1])

win = f[1] if len(f[0]) == 0 else f[0]
total = 0
for i,n in enumerate(win[::-1]):
    total += (i+1)*n
print(total)
