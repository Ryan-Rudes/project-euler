def update(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def chain(n, length=0):
	global chainlength
	
	if n == 1:
		return length
	else:
		if not n in chainlength:
			chainlength[n] = None
			
		if chainlength[n] is None:
			final = chain(update(n), length = length + 1)
			chainlength[n] = final - length
			return final
		else:
			return length + chainlength[n]
			
T = int(input().strip())
N = [int(input().strip()) for i in range(T)]

chainlength = {n + 1:None for n in range(max(N))}
chainlength[1] = 0

for n in range(max(N)):
	chain(n + 1)
	
chainlength = [chainlength[i + 1] for i in range(max(N))]
	
solutions = {}
indices = [0]
value = chainlength[1]
for i, e in enumerate(chainlength):
    if e > value:
        indices = [i]
        value = e
    elif e == value:
        indices.append(i)
        
    solutions[i + 1] = max(indices) + 1
    
for n in N:
    print (solutions[n])
