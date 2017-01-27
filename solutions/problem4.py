def largestPanlindromePdt():
    palindrome = 0

    for n1 in range(1000, 100, -1):
        for n2 in range(1000, 100, -1):
            pdt = n1 * n2
            if str(pdt) == str(pdt)[::-1] and  pdt > palindrome:
                palindrome = pdt
    return palindrome

print(largestPanlindromePdt())
