T = int(input().strip())
for i in range(T):
    N = int(input().strip())

    while N % 2 == 0:
        greatestPrimeFactor = 2
        N //= 2
    
    for i in range(3, int(N ** 0.5) + 1, 2):
        while N % i == 0:
            greatestPrimeFactor = i
            N //= i

    if N > 2:
        greatestPrimeFactor = N
        
    print (greatestPrimeFactor)
