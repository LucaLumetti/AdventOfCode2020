f = open('input').readlines()
t = 0
for l in f:
    l = l[0:-1][::-1] + "\n"
    l = l.replace('(',']')
    l = l.replace(')','[')
    l = l.replace(']',')')
    l = l.replace('[','(')

    new_str = ""
    open_b = [0]
    inside = 0

    for c in l:
        if c != '\n':
            new_str += c
            continue
        if c == '*' or c == '+':
            new_str += '('
            open_b[inside] += 1
            continue
        if c == '(':
            open_b.append(0)
            inside += 1
            continue
        if c == ')' or c == '\n':
            new_str += ')'*open_b[inside]
            open_b[inside] = 0
            inside -= 1
            continue

    t += eval(new_str)
print(t)
