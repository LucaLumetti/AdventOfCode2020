import re
f = open('input','r').read()
f = f.rstrip().split('\n\n')
v = 0

for p in f:
    p = p.replace('\n', ' ')
    byr = re.search(r'byr:', p)
    iyr = re.search(r'iyr:', p)
    eyr = re.search(r'eyr:', p)
    hgt = re.search(r'hgt:', p)
    hcl = re.search(r'hcl:', p)
    ecl = re.search(r'ecl:', p)
    pid = re.search(r'pid:', p)
    v += not not(byr and iyr and eyr and hgt and hcl and ecl and pid)
print(v)
