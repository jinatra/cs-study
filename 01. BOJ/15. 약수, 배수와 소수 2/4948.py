import sys

MAX = 123456 * 2

prime = [True] * (MAX + 1) # 전체 숫자만큼 
prime[0] = False
prime[1] = False # 0과 1은 소수 아닌거 체크

root = int(MAX ** 0.5)

for i in range(2, root + 1): # 소수 구하는 부분
    if prime[i]:
        for j in range(i*2, MAX + 1, i):
            prime[j] = False

# 이제 체크
while True:
    n = int(sys.stdin.readline())
    ans = 0
    if n == 0:
        break
    for i in range(n+1, 2*n+1):
        if prime[i] == True:
            ans += 1
    print(ans)