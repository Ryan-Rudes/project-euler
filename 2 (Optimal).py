import sys

"""
The nth fibonacci number:
f(n) = f(n - 2) + f(n - 1)

The nth EVEN fibonacci number:
f(n) = f(n - 2) + f(n - 1) * 4
"""

T = int(input().strip())
for i in range(T):
    N = int(input().strip())

    n0 = 0
    n1 = 2
    total = 0
    
    while n0 <= N:
        total += n0
        n0, n1 = n1, n0 + n1 * 4
        
    print (total)
