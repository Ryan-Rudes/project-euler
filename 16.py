T = int(input().strip())
for i in range(T):
    N = int(input().strip())
    print (sum([int(digit) for digit in str(2 ** N)]))
    
"""
Or the absurd one-line solution:
[print (sum([int(digit) for digit in str(2 ** int(input().strip()))])) for i in range(int(input().strip()))]
"""
