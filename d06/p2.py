import functools
f = open('input','r').read().rstrip().split('\n\n')
f = [ [set(s) for s in l.split('\n')] for l in f ]
print(sum([ len(functools.reduce(lambda x,y: x.intersection(y), e)) for e in f]))
