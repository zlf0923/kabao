from collections import Iterable
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k, v in d.items():
    print(k,v)

for ch in 'ABCD':
    print(ch)

ib = isinstance('abc', Iterable) #str是否可迭代
print(ib)

ib1 = isinstance([1,2,3],Iterable)#list是否可迭代
print(ib1)

ib2 = isinstance(123,Iterable)#整数是否可迭代
print(ib2)


for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


















