import re
f = open('input','r').read()
f = f.rstrip().split('\n\n')
v = 0

for p in f:
    p = p.replace('\n', ' ')
    byr = re.search(r'byr:(19[2-9][0-9]|200[0-2])', p)
    iyr = re.search(r'iyr:(201[0-9]|2020)', p)
    eyr = re.search(r'eyr:(202[0-9]|2030)', p)
    hgt = re.search(r'hgt:(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)', p)
    hcl = re.search(r'hcl:#[0-9a-f]{6}', p)
    ecl = re.search(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)', p)
    pid = re.search(r'pid:[0-9]{9}( |$)', p)
    v += not not(byr and iyr and eyr and hgt and hcl and ecl and pid)
print(v)
