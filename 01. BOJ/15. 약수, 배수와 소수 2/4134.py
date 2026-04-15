import sys

# 소수 판별
# 소수면 True
def is_prime(n):
    root = int(n ** 0.5)
    if n < 2:
        return False # 0,1 은 소수 아님
    for i in range(2, root + 1):
        if n % i == 0:
            return False # 나눠 떨어지면 소수 아님
    return True # 전부 소수

n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    while True:
        if is_prime(num) == False:
            num += 1
        else:
            print(num)
            break