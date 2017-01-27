import math

def findPrimeUptoCount(count, limit):

    '''
        Solution using Eratosthenes theorem
    '''

    isPrime = {}

    isPrime[1] = False

    # Initially set all numbers to true
    for i in range(2, limit + 1):
        isPrime[i] = True

    # Set the multiples of initial number to false
    for i in range(2, int(math.sqrt(limit)) + 1):
        for j in range(2, limit + 1):
            if isPrime[i]:
                k = i * j
                if k > limit:
                    break
                isPrime[k] = False

    primeArr = []
    primeNumbers = 0
    
    # True values are the required prime numbers
    for i in range(2, limit + 1):
        if isPrime[i]:
            primeNumbers += 1
            if primeNumbers > count:
                break
            primeArr.append(i)
    return primeArr

result = findPrimeUptoCount(10001, 110000)
print(result[len(result) - 1])
