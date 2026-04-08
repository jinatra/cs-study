import sys
input = sys.stdin.readline

N = int(input())
count = [0] * 10001 #숫자범위

for _ in range(N):
    count[int(input())] += 1

result = []
for i in range(1, 10001):
    if count[i] > 0:
        result.append((str(i) + '\n') * count[i])

sys.stdout.write(''.join(result))