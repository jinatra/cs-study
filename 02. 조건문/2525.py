A, B = map(int, input().split())
C = int(input())

H = (B+C) // 60 # 초과되는 시간
M = (B+C) % 60 # 초과되는 분

if A + H < 24:
    print(f'{A+H} {M}')
else:
    print(f'{(A+H)-24} {M}')
