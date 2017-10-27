def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(1))
print(fact(5))
print(fact(100))

def fact1(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact_iter(1000,1))
