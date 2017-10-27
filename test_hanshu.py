def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end())
print(add_end())
print(add_end())

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([1, 2, 3]))
print(calc((1, 3, 5, 7)))

#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2))
print(calc())

nums = [1,2,3]
print(calc(*nums))


#关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


#命名关键字参数
def person1(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)
person1('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

def person2(name, age, *, city, job):
    print(name, age, city, job)
person2('Jack', 24, city='Beijing', job='Engineer')

def person3(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person3('Jack', 24, job='Engineer')


#参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f2(1, 2, d=99, ext=None)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)


def hello(greeting, *args):
    if(len(args)==0):
        print('%s!' % greeting)
    else:
       print('%s, %s!' % (greeting, ', '.join(args)))
hello('Hi')
hello('Hi', 'Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names)


def print_scores(**kw):
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s  %d' % (name, score))
    print()

print_scores(Adam=99, Lisa=88, Bart=77)
        
data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
    }

print_scores(**data)


def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()

print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)






















