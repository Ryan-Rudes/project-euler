T = int(input())

def fact(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
        
    return res

for i in range(T):
    N = int(input())
    print (sum([int(digit) for digit in str(fact(N))]))
