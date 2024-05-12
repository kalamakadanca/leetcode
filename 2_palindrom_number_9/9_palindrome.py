#Given an integer x, return true if x is a palindrome, and false otherwise.


def isPalindrome(x):
    x = str(x)
    if x[0] == "-":
        return False
    for i in range(len(x)):
        if x[i] != x[-i - 1]:
            return False
    return True








print(isPalindrome(121))
#true
print(isPalindrome(-121))
#false
print(isPalindrome(10))
#false