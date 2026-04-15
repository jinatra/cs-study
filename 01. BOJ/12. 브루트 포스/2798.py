import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))

ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            s = num_list[i]+num_list[j]+num_list[k]
            if s <= M and s >= ans:
                ans = s

print(ans)