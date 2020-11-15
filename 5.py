import sys

T = int(input().strip())
for i in range(T):
    N = int(input().strip())
    
    num = N
    while True:
        divisible = True
        for i in range(2, N + 1):
            if num % i != 0:
                divisible = False
                break
    
        if divisible:
            break
        else:
            num += 1
        
    print (num)
