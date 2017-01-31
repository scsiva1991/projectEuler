import math

def getPrimeNumbersByRange(limit):
    isPrime = {}

    isPrime[1] = False

    for i in range(2, limit + 1):
        isPrime[i] = True

    for i in range(2, int(math.sqrt(limit)) + 1):
        for j in range(2, limit + 1):
           k = i * j
           if k > limit:
               break
           isPrime[k] = False

    primeArr = []
    for i in range(2, limit + 1):
        if isPrime[i]:
            primeArr.append(i)

    return primeArr

def sumOfPrime(limit):
    return sum(getPrimeNumbersByRange(limit))

print(sumOfPrime(2000000))