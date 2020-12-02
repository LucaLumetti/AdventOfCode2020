import re
f = open('input', 'r').readlines()

vpwd = 0
for s in f:
    regex = r"(\d+)\-(\d+)\ ?(.)\:\ (.*)"
    m = re.match(regex, s, re.MULTILINE)
    a,b,c,d = m.groups()
    a,b = int(a), int(b)
    count = s.count(c)
    vpwd += count >= a and count <= b
print(vpwd)
