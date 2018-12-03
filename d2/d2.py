xs = open("inp.txt").read().split()

count2 = count3 = 0

for s in xs:
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    if 2 in d.values():
        count2 += 1
    if 3 in d.values():
        count3 += 1

print("Answer:", count2 * count3)
