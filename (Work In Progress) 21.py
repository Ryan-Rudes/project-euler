def prime_factorize(n):
    factorization = {}
    if n % 2 == 0:
        factorization[2] = 0
        while n % 2 == 0:
            n //= 2
            factorization[2] += 1
            
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            factorization[i] = 0
            while n % i == 0:
                n //= i
                factorization[i] += 1
    
    if n > 2:
        factorization[n] = 1
        
    return factorization

def prod(vec):
    res = 1
    for i in vec:
        res *= i
        
    return res

def f(N):
    factorization = prime_factorize(N)
    return prod([sum([base ** i for i in range(1, exponent + 1)]) + 1 for base, exponent in factorization.items()])

T = int(input())
N = [int(input()) for i in range(T)]
maxN = max(N)
j = [f(i) for i in range(maxN)]
for i, x in enumerate(j):
    if j[x - 1] == i:
        total += 1
