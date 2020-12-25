from math import ceil, sqrt

def bsgs(g, h, p):
    N = ceil(sqrt(p - 1))
    tbl = {pow(g, i, p): i for i in range(N)}
    c = pow(g, N * (p - 2), p)
    for j in range(N):
        y = (h * pow(c, j, p)) % p
        if y in tbl:
            return j * N + tbl[y]
    return None

c_pk, s_pk = [ int(l.rstrip()) for l in open('input').readlines() ]
print(pow(s_pk, bsgs(7, c_pk, 20201227), 20201227))
