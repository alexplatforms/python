L0 = []

L1 = L0 + [1]

L1[len(L1):] = [2]
L1.append(3)

L1[len(L1):] = {4, 5, 6}
L1.extend({7, 8, 9})

print(L1)
