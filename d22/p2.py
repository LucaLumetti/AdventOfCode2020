f = [ l.split('\n')[1:] for l in open('input').read().rstrip().split('\n\n') ]
f[0] = [ int(n) for n in f[0] ]
f[1] = [ int(n) for n in f[1] ]

history = {}

# function to convert a state to a string, to use it in history hash map
def state_to_str(p1,p2):
    str1 = ','.join([str(a) for a in p1])
    str2 = ','.join([str(b) for b in p2])
    return f"P1:{str1};P2:{str2}"

def check_history(p1,p2):
    s = state_to_str(p1,p2)
    # check if the state has been seen before
    if(s in history): return True
    # hash the state of the game and save it
    history[s] = 1
    return False

def game(p1,p2, g):
    if(len(p1) == 0):
        return 1,p1,p2
    if(len(p2) == 0):
        return 0,p1,p2
    r = 1
    while(True):
        if(len(history) % 1000000 == 0):
            print(f"G{g},R{r} ({len(history)/1000000})")
        r+=1

        # check if the game has been played before
        r1 = check_history(p1,p2)
        if(r1): return 0, p1, p2

        # draw the first card, a is the p1 card and b is the p2 card
        a,b = p1[0], p2[0]
        p1, p2 = p1[1:], p2[1:]

        round_winner = None
        # the sub-game rule
        if(len(p1) >= a and len(p2) >= b):
            round_winner, _, __ = game(p1.copy(),p2.copy(), g+1)
        else:
            round_winner = 0 if a > b else 1

        # add the cards to the winner's deck
        if(round_winner == 0):
            p1.extend([a,b])
        else:
            p2.extend([b,a])

        # check if someone has won
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
