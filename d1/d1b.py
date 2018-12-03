xn = [int(x) for x in open("inp.txt").read().split()]

found = False
s = 0
freq = set()

while not found:
    for x in xn:
        s += x
        if s in freq:
            found = True
            break
        freq.add(s)

print("Answer:", s)




