def checkDivisibility():
    '''
        Divide by 20 will check for 2, 4, 5, 10
        Divide by 18 will check for 6, 3
        Divide by 16 will check for 8
        Divide by 14 will check for 7
    '''
    checkList = [11, 13, 14, 16, 17, 18, 19, 20]

    '''
        Since a number needs to be divisible by 20 and all numbers
        less than 20, lets start from 20 and increase by 20
    '''
    for i in range(20, 9999999999999, 20):
        if all(i % n == 0 for n in checkList):
            return i
    return -1

result = checkDivisibility()
if result > -1:
    print("Smallest multiple is %d" %result)
else:
    print("No results found")
