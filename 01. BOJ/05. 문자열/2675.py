import sys
T = int(sys.stdin.readline())

for i in range(T):
    R, S = sys.stdin.readline().rstrip().split()
    ans = ''
    for i in S:
        ans += i*int(R)
    print(ans)