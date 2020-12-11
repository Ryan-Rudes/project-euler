from math import gcd

lcm = lambda x, y: x * y // gcd(x, y)

T = int(input())
for i in range(T):
    N = int(input())
    if N == 1:
        print (1)
    else:
        res = 2
        for j in range(3, N + 1):
            res = lcm(res, j)
            
        print (res)
