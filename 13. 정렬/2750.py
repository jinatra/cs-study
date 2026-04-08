import sys

N = int(sys.stdin.readline())

l = []
for _ in range(N):
    i = int(sys.stdin.readline())
    l.append(i)
l.sort()
for i in l:
    print(i)