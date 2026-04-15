import sys

N = int(sys.stdin.readline())

l = []
for i in range(1600):
    for j in range(1600):
        if 3*i + 5*j == N:
            l.append(i+j)

if len(l) == 0:
    print(-1)
else:
    print(min(l))
