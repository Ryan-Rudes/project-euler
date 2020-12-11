a = {}

for i in range(2, 200000):
  if not i in a:
    for j in range(2 * i, 200000, i):
      a[j] = 1

p = []
for i in range(2, 200000):
  if not i in a:
    p.append(i)

T = int(input())
for i in range(T):
    N = int(input())
    print (p[N - 1])
