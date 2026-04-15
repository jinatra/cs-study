import sys

N = int(sys.stdin.readline())

l = []
for i in range(N):
    l.append(i+1)

while len(l) != 1:
    del l[0]
    f = l[0]
    l.append(f)
    del l[0]

print(l[0])