import sys

"""
(1^2+...+n^2) = n*(n+1)*(2*n+1)/6
(1+2+...+n)^2 = (n*(n+1)/2)^2
"""

T = int(input().strip())
for i in range(T):
    N = int(input().strip())
    
    sum_of_squares = N * (N + 1) * (2 * N + 1) / 6
    square_of_sum = (N * (N + 1) / 2) ** 2
    print (int(abs(sum_of_squares - square_of_sum)))
