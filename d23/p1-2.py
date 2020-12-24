from itertools import count
f = [int(c) for c in open("input").read().rstrip()]

def play(cups, num_iterations):
    max_cup = max(cups)
    min_cup = min(cups)
    d = {c1: c2 for c1, c2 in zip(cups, cups[1:] + [cups[0]])}
    cur = cups[0]
    for x in range(num_iterations):
        x = cur
        pickup = []
        for _ in range(3):
            pickup.append(d[x])
            x = d[x]

        cup = cur-1
        for i in count(1):
            cup = cur-i if cup > 0 else len(cups)+cup
            if(cup not in pickup): break
        if(cup <= 0): cup = len(cups)+cup
        dest = cup
        d[cur], d[pickup[-1]], d[dest] = d[pickup[-1]], d[dest], d[cur]

        cur = d[cur]

    x = 1
    return [x := d[x] for _ in cups]


part1 = play(f, 100)
print("".join(str(x) for x in part1[:-1]))

part2 = play(f + list(range(len(f) + 1, 1000000 + 1)), 10000000)
print(part2[0] * part2[1])
