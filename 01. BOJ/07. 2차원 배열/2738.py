import sys

N, M = map(int, sys.stdin.readline().split())

A = []
B = []
for i in range(N):
    nums = list(map(int, sys.stdin.readline().split()))
    A.append(nums)
for i in range(N):
    nums = list(map(int, sys.stdin.readline().split()))
    B.append(nums)

ans = []
for i in range(N):
    rows = []
    for j in range(M):
        rows.append(A[i][j]+B[i][j])
    ans.append(rows)

for row in ans:
    print(' '.join(map(str, row)))