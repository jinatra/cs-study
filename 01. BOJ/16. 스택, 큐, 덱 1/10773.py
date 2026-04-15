import sys

K = int(sys.stdin.readline())

ans = []
for _ in range(K):
    n = int(sys.stdin.readline())
    if n == 0:
        ans.pop()
    else:
        ans.append(n)

print(sum(ans))