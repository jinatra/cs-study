import sys

N = int(sys.stdin.readline())

total = 1
n = 1

while total < N:
    total += n*6
    n += 1

print(n)




# 2: 6 (2~7)
# 3: 12 (8~19)
# 4: 18 (20~37)
# 5: 24 (38~61)