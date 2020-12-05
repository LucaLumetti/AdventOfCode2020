f = open('input','r').readlines()
s = [ int(l.replace('F','0').replace('B','1')[:-4],2)*8+int(l.replace('R','1').replace('L','0')[-4:],2) for l in f ]
print((set(range(min(s),max(s))) - set(s)).pop())
