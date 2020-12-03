T = int(input())
N = [int(input()) for i in range(T)]
maxN = max(N)
chainLengths = {1:1}

def updateRule(n):
  if n % 2 == 0:
    return n // 2
  else:
    return 3 * n + 1
  
def updateChain(n):
  global chainLengths
  
  if n in chainLengths:
    return chainLengths[n]
  else:
    chainLengths[n] = updateChain(updateRule(n)) + 1
    return chainLengths[n]
  
for i in range(2, maxN + 1):
  updateChain(i)
  
res = {}
y = 0
maxLength = 0
for i in range(1, maxN + 1):
  if chainLengths[i] >= maxLength:
    maxLength = chainLengths[i]
    y = i
      
  res[i] = y
  
for n in N:
  print (res[n])
