f = open('input').read().split('\n\n')

rt = f[0].splitlines()
rules = {}
for r in rt:
    spl = r.split(': ')
    rules[spl[0]] = [e.split(' ') for e in spl[1].split(' | ')]

s = f[1].splitlines()

def check(rules, key, l, start):
    rule = rules[key]
    if rule[0][0][0] == '"': return {start + 1} if start < len(l) and  rule[0][0][1] == l[start] else set()
    endings = set()
    for subrule in rule:
        buffer = {start}
        for part in subrule:
            temp = set()
            for loc in buffer:
                temp = temp | check(rules, part, l, loc)
            buffer = temp
        endings = endings | buffer
    return endings

print(sum([len(l) in check(rules, '0', l, 0) for l in s]))
rules['8'] = [['42'],['42','8']]
rules['11'] = [['42','31'],['42','11','31']]
print(sum([len(l) in check(rules, '0', l, 0) for l in s]))
