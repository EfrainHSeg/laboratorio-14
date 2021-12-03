def fib(n):
    a = 0
    b = 1

    while a < n:
        print(a, end =' ')
        a, b = b, a + b

    return "finish"

def f_suma(xy) :
    a = 0
    b = 1
    
    suma= 0

    while a < xy:
        print(a, end=' ')

        a, b = b, a + b

        suma= suma+b

    return suma

def fac (num) :
    fact = 1

    while (num != 0):
        fact = fact * num
        num = num = 1
        return fact
