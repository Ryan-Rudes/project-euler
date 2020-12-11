import sys

def summation(n):
    """Returns the sum of all natural numbers in [1, n]"""
    return n * (n + 1) // 2
    
T = int(input().strip())
for i in range(T):
    N = int(input().strip())

    mult3 = (N - 1) // 3
    mult5 = (N - 1) // 5
    mult15 = (N - 1) // 15
        
    sum3 = 3 * summation(mult3)
    sum5 = 5 * summation(mult5)
    sum15 = 15 * summation(mult15)
    
    print (sum3 + sum5 - sum15)
