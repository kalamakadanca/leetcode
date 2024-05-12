def isPalindrome(x):
    #x = len(x) / 2
    for i in range(x//2):
        x = str(x)
        print(x[i])
        print(i)
        print(x[-i])
        print(-i)
        if x[i] != x[-1]:
            return False
    return True