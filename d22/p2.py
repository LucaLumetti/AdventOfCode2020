f = [ l.split('\n')[1:] for l in open('input').read().rstrip().split('\n\n') ]
f[0] = [ int(n) for n in f[0] ]
f[1] = [ int(n) for n in f[1] ]

history = {}
def state_to_str(p1,p2):
    str1 = ','.join([str(a) for a in p1])
    str2 = ','.join([str(b) for b in p2])
    return f"P1:{str1};P2:{str2}"

def check_history(p1,p2):
    s = state_to_str(p1,p2)
    if(s in history): return True
    history[s] = 1
    return False

def game(p1,p2, g):
    if(len(p1) == 0):
        return 1,p1,p2
    if(len(p2) == 0):
        return 0,p1,p2
    r = 1
    while(True):
        if(len(history) % 100000 == 0):
            print(f"G{g},R{r} ({len(history)})")
        r+=1

        r1 = check_history(p1,p2)
        if(r1): return 0, p1, p2
        a,b = p1[0], p2[0]
        p1, p2 = p1[1:], p2[1:]
        round_winner = None
        if(len(p1) >= a and len(p2) >= b):
            round_winner, _, __ = game(p1.copy(),p2.copy(), g+1)
        else:
            round_winner = 0 if a > b else 1

        if(round_winner == 0):
            p1.extend([a,b])
        else:
            p2.extend([b,a])
        if(len(p1) == 0):
            return 1, p1, p2
        if(len(p2) == 0):
            return 0, p1, p2

def calculate_points(deck):
    total = 0
    for i,n in enumerate(deck[::-1]):
        total += (i+1)*n
    return total

winner, p1, p2 = game(f[0], f[1],0)

if(winner == 0):
    print(calculate_points(p1))
else:
    print(calculate_points(p2))
