import sys

N = int(sys.stdin.readline())

cnt = 0
ans = 0

for n in range(10000000):
    if '666' in str(n):
        cnt += 1
        ans = n
        if cnt == N:
            print(ans)
            break