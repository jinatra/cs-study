import sys

M, N = map(int, sys.stdin.readline().rstrip().split())

# 소수면 True
def is_prime(n):
    if n < 2: # 2보다 작으면 소수 아님
        return False
    root = int(n ** 0.5)
    for i in range(2, root + 1): # 제곱근까지 나뉘어지는 수 없으면
        if n % i == 0:
            return False
    return True

for n in range(M, N + 1):
    if is_prime(n):
        print(n)
    else:
        pass