import sys

N = int(sys.stdin.readline())

for n in range(1, N+1):
    l = [n]
    for i in str(n):
        l.append(int(i))
    
    if sum(l) == N:
        print(n)
        break
else:
    print(0)