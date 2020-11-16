T = int(input().strip())
for i in range(T):
    N, M = input().strip().split(' ')
    N, M = int(N), int(M)

    P0 = [1] * N
    for i in range(M):
        p = 1
        P1 = []
        for i in P0:
            p += i
            P1.append(p)
        
        P0 = P1
        
    print (P0[-1] % (10 ** 9 + 7))
