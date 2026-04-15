import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

s = set()

for _ in range(N):
    s.add(sys.stdin.readline().rstrip())

ans = []
for _ in range(M):
    name = sys.stdin.readline().rstrip()
    if name in s:
        ans.append(name)

print(len(ans))
ans.sort()
for a in ans:
    print(a)