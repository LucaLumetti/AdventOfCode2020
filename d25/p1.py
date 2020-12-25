c_pk, s_pk = [ int(l.rstrip()) for l in open('input').readlines() ]
subj, r = 7, s_pk
while(True):
    subj = (subj*7)%20201227
    r = (s_pk*r)%20201227
    if(subj == c_pk): break
print(r)
