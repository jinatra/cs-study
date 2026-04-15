import sys

A = list(map(int, sys.stdin.readline().split()))

# 1 1 2 2 2 8
ans = []
for i in range(len(A)):
    if 0 <= i < 2:
        ans.append(str(1 - int(A[i])))
    elif 2 <= i < 5:
        ans.append(str(2 - int(A[i])))
    else:
        ans.append(str(8 - int(A[i])))

print(' '.join(ans))

# chess = [1, 1, 2, 2, 2, 8]

# for i in range(len(chess)):
#     print(chess[i] - A[i], end = ' ')