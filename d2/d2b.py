xs = open("inp.txt").read().split()

found = False

for s in xs:
    for t in xs:
        if [s[i] == t[i] for i in range(len(s))].count(False) == 1:
            found = True
            b1, b2 = s, t
            break
    if found:
         break

print(b1)
print(b2)

for i in range(len(b1)):
    if b1[i] != b2[i]:
        index = i

print("Answer:", b1[:index] + b1[index+1:])

