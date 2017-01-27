def findSquareDiff(n):

    '''
        To find sum of squares of first n natural numbers
        (n * (n + 1) * (2n + 1) )/ 6
    '''

    sum1 = (n * (n + 1) * (2 * n + 1)) / 6

    '''
        To find sum of first n natural numbers
        (n * n+1)/2
    '''

    sum2 = (n * (n + 1)) / 2 

    return int(sum2 ** 2 - sum1)

print(findSquareDiff(100))
