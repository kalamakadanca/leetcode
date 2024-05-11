#Given an integer x, return true if x is a palindrome, and false otherwise.


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







print(isPalindrome(121))
#true
print(isPalindrome(-121))
#false
print(isPalindrome(10))
#false