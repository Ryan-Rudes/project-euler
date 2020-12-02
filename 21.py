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

T = int(input())
N = [int(input()) for i in range(T)]
maxN = max(N)
d = {}
amicable = set()

for a in range(2, maxN + 1):
    if not a in d:
      d[a] = sumDivisors(a)
    
    b = d[a]

    if not b in d:
      d[b] = sumDivisors(b)

    if a != b:
      if d[b] == a:
        if not a in amicable:
          amicable |= {a}

        if not b in amicable:
          amicable |= {b}

amicable = sorted(list(amicable))

for n in N:
  y = 0
  for x in amicable:
    if x >= n:
      break
    else:
      y += x

  print (y)
