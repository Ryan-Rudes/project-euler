import sys

def primes_not_above(N):
    prime = {i:True for i in range(N + 1)}
    p = 2
    
    while p ** 2 <= N:
        if prime[p]:
            for i in range(p ** 2, N + 1, p):
                prime[i] = False
                
        p += 1
        
    return prime

T = int(input().strip())
N = [int(input().strip()) for i in range(T)]
maxN = max(N)

primes = primes_not_above(maxN)

total = 0
totals = {}
for value, isprime in primes.items():
    if isprime:
        total += value
    
    totals[value] = total

for n in N:
    print (totals[n] - 1)
