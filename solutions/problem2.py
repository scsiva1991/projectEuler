def fib(limit):
    a, b, sum = 0, 1, 0
    while a < limit:
        if a % 2 == 0:         
            sum += a
        a, b = b, a + b
    return sum

print (fib(4000000))