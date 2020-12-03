from math import log, ceil

phi = (1 + 5 ** 0.5) / 2
T = int(input())

for i in range(T):
    N = int(input())
    res = ceil((log(10) * (N - 1) + log(5) / 2) / log(phi))
    print (res)
