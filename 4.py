def search(l, n):
  if len(l) == 1:
    return l[0]

  i = len(l) // 2
  x = l[i]

  if n > x:
    return search(l[i:], n)
  elif n == x:
    return l[i - 1]
  else:
    return search(l[:i], n)

palindrome = lambda n: str(n) == str(n)[::-1]
products = []

for x in range(100, 1000):
  for y in range(100, 1000):
    product = x * y
    if palindrome(product):
      products.append(product)

products = list(set(products))
products.sort()

T = int(input())
for i in range(T):
    N = int(input())
    print (search(products, N))
