f = open('input','r').read().split('\n\n')
f = [ set(l.replace('\n','')) for l in f ]
print(sum([ len(s) for s in f ]))
