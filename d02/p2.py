import re
f = open('input', 'r').readlines()

vpwd = 0
for s in f:
    r = r"(\d+)\-(\d+)\ ?(.)\:\ (.*)"
    m = re.match(r, s, re.MULTILINE)
    a,b,c,d = m.groups()
    a,b = int(a),int(b)
    vpwd += (d[a-1]+d[b-1]).count(c) == 1
print(vpwd)
