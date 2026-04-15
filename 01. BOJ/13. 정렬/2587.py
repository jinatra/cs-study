import sys

l = []
for _ in range(5):
    l.append(int(sys.stdin.readline()))

l.sort()
print(int(sum(l)/len(l)))
print(l[2])