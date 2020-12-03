N = int(input())

f = lambda x, N: sum([int(digit) ** N for digit in str(x)])
x = 0
total = 0
streak = 0

while True:
    diff = f(x, N) - x
    if diff == 0:
        total += x
        streak = 0
    elif diff > 0:
        streak = 0
    else:
        streak += 1
        
    x += 1
    
    if streak == 1000:
        break
    
print (total - 1)
