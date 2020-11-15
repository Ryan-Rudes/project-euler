import sys

"""
To check efficiently if a number is prime, consider all potential prime factors between 2 and floor(sqrt(N)), inclusive.
When generating a list of primes, we don't want to have to find all primes beneath N for each time we check N, so we record
a list of each prime, then we can limit how many numbers we actually need to check as potential factors. If we compute this
list of primes beforehand, we can then just index each N provided in the test cases, so the printing of the output all happens
instantaneously at the end.
"""

def generate_primes():
    primes = [2]
    yield 2
    prime = 3
    while True:
        for factor in primes:
            if factor < int(prime ** 0.5) + 1:
                if prime % factor == 0:
                    isprime = False
                    break
            else:
                isprime = True
                break
        
        if isprime:
            primes.append(prime)
            yield prime
            
        prime += 2
        
T = int(input().strip())
generator = generate_primes()

N = [int(input().strip()) for i in range(T)]
primes = [next(generator) for i in range(max(N))]
for n in N:
    print (primes[n - 1])
