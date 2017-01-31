import time

start = time.time()

def isPythagoreanTriplet(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    return False

def checkPythagoreanTriplet():

    for a in range(1, 1000):
        for b in range(a, 1000 - a):
            for c in range(b, 1000 - b):
                if a + b + c == 1000:
                    if isPythagoreanTriplet(a, b, c):
                        elapsed = time.time() - start
                        print(a, b, c)
                        print("Time: {:.5f} seconds".format(elapsed))
                        return(a * b * c)

print(checkPythagoreanTriplet())