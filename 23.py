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

def geomSum(r, n):
    return (r ** n - 1) // (r - 1)

def sumDivisors(n):
    return prod([geomSum(base, exponent + 1) for base, exponent in prime_factorize(n).items()]) - n

def sumPairs(n):
  for i in range(1, n // 2 + 1):
    yield i, n - i

T = int(input())
N = [int(input()) for i in range(T)]
maxN = max(N)

abundant = {i:sumDivisors(i) > i for i in range(1, maxN)}

for i in N:
  yes = False
  for a, b in sumPairs(i):
    if abundant[a] and abundant[b]:
      yes = True
      break

  print ("YES" if yes else "NO")
