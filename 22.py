N = int(input())
names = sorted([input() for i in range(N)])
nameScore = lambda name: sum([ord(char) - 64 for char in name])
Q = int(input())
for i in range(Q):
    name = input()
    idx = names.index(name)
    print ((idx + 1) * nameScore(name))
