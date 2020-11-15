# Not the most efficient solution, but it passes all of the test cases in time.

import sys

def is_palindrome(num):
    return str(num) == str(num)[::-1]

T = int(input().strip())
for i in range(T):
    N = int(input().strip())
    
    maxPalindrome = 0

    for x in reversed(range(100, 1000)):
        for y in reversed(range(100, x + 1)):
            prod = x * y
            
            if prod < N and prod > maxPalindrome and is_palindrome(prod):
                maxPalindrome = prod
                
    print (maxPalindrome)
