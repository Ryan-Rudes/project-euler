T = int(input().strip())

def gen_factors(n):
    yield 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        yield i
        
for i in range(T):
    N = int(input().strip())

    for i in gen_factors(N):
        while N % i == 0:
            largest = i
            N //= i

    if N > 2:
        largest = N
        
    print (largest)
