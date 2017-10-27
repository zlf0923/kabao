L = list(range(1, 11))
print(L)

L1 = []
for x in range(1,11):
    L1.append(x*x)
print(L1)

L2 = [x * x for x in range(1, 11)]
print(L2)

L3 = [x * x for x in range(1,11) if x % 2 ==0]
print(L3)

L4 = [m + n for m in 'ABC' for n in 'XYZ']
print(L4)

import os
L5 = [d for d in os.listdir('.')]#列出文件和目录
print(L5)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

d1 = {'x': 'A', 'y': 'B', 'z': 'C' }
L6 = [k + '=' + v for k, v in d1.items()]
print(L6)

d2 = ['Hello', 'World', 'IBM', 'Apple']
L7 = [s.lower() for s in d2]#变小写
print(L7)

d3 = ['Hello', 'World', 18, 'Apple', None]
L8 = [s.lower() for s in d3 if isinstance(s,str)]#仅列出字符串
print(L8)
















