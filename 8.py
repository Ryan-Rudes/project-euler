import sys

def prod(string):
    product = 1
    for digit in string:
        product *= int(digit)
        
    return product

T = int(input().strip())
for i in range(T):
    N, K = input().strip().split(' ')
    N, K = [int(N), int(K)]
    num = input().strip()
    print (max([prod(num[i:i + K]) for i in range(len(num) - K + 1)]))
