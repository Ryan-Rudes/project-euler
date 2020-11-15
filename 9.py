import sys

T = int(input().strip())
for i in range(T):
    N = int(input().strip())
    
    maxProd = -1
    for a in range(3, N // 3):
        b = (N ** 2 - 2 * N * a) / (2 * N - 2 * a)
        if b == int(b):
            c = N - (a + b)
            if a ** 2 + b ** 2 == c ** 2:
                maxProd = max(maxProd, a * b * c)

    print (int(maxProd))
