L0 = []

L1 = L0 + [1]  # L1: [1]
print(L1)

L1[len(L1):] = [2] # L1: [1, 2]
print(L1)

L1.append(3) # L1: [1, 2, 3]
print(L1)

L1[len(L1):] = {4, 5, 6} # L1: [1, 2, 3, 4, 5, 6]
print(L1)

L1.extend({7, 8, 9})  # L1: [1, 2, 3, 4, 5, 6, 8, 7] NOTE!
print(L1)

L1.insert(0, 0)  # L1: [0, 1, 2, 3, 4, 5, 6, 8, 9, 7]
print(L1)

L1.insert(len(L1), 10)  # L1: [0, 1, 2, 3, 4, 5, 6, 8, 9, 7, 10]
print(L1)

L1.insert(1, 2)  # L1: [0, 2, 1, 2, 3, 4, 5, 6, 8, 9, 7, 10]
print(L1)

L1.remove(2)  # L1: [0, 1, 2, 3, 4, 5, 6, 8, 9, 7, 10]
print(L1)

p = L1.pop()  # L1: [0, 1, 2, 3, 4, 5, 6, 8, 9, 7]
print(L1)

p = L1.pop(0)  # L1: [1, 2, 3, 4, 5, 6, 8, 9, 7]
print(L1)
