import sys

N = int(sys.stdin.readline())

n = 2
for i in range(N):
    n = (n * 2) -1
print(n**2)

# 0 : 2
# 1 : 3
# 2 : 5
# 3 : 9
# 4 : 17