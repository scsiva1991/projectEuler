import math

def findPrimeFactor(num):
    # To check given number is divisible by 2
    while(num % 2 == 0):
        print(2)
        num /= 2

    # If number is divisible by 2 it will be odd
    for i in range(3, int(math.sqrt(num)), 2):
        if(int(num) % i == 0):
            print(i)
            num /= i

    # From the above two methods given number will always greater than 2
    if num > 2 :
        print(int(num))

findPrimeFactor(600851475143)
