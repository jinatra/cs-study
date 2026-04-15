import sys

# 체 만들기
MAX = 1000000
is_prime = [True] * (MAX + 1)
is_prime[0] = False
is_prime[1] = False

root = int(MAX ** 0.5)
for i in range(2, root + 1):
    if is_prime[i]:
        for j in range(2*i, MAX + 1, i):
            is_prime[j] = False

# 소수 리스트
primes = []
for i in range(len(is_prime)):
    if is_prime[i] == True:
        primes.append(i)

# 문제 계산
T = int(sys.stdin.readline())
for _ in range(T):
    num = int(sys.stdin.readline())
    ans = 0
    for p in primes:
        if p > num // 2: # 절반보다 높으면 이미 있는거니까 패스
            break
        if is_prime[num-p]:
            ans += 1
    print(ans)