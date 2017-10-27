L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L)

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-1])
print(L[-2:])
print(L[-2:-1])

L1 = list(range(100))
print(L1)
print('L1[:10]:', L1[:10])
print('L1[-10:]:', L1[-10:])
print('L1[10:20]:', L1[10:20])
print('L1[:10:2]:', L1[:10:2])
print('L1[::5]:', L1[::5])
print(L1[:])

T = (0, 1, 2, 3, 4, 5)[:3]
print(T)

S = 'ABCDEFGH'[:3]
print(S)

S1 = 'abcdefghijk'[::2]
print(S1)
