def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5))

def enroll(name, gender, age = 6, city='Shanghai'):
    print('name:', name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

enroll('Bob', 'M')



