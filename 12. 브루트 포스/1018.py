import sys

N, M = map(int, sys.stdin.readline().split())

board = []

for _ in range(N):
    board.append(sys.stdin.readline().strip())

count = []
for r in range(N-7):
    for c in range(M-7):
        # board[r][c]부터 [r+7][c+7]까지가 8X8 영역
        cnt = 0
        for i in range(r, r+8):
            for j in range(c, c+8):
                if (i+j) % 2 == 0: # 짝수
                    if board[i][j] != 'W': # 짝수칸이 W라고 가정했는데 W가 아니면
                        cnt += 1
                else:              # 홀수
                    if board[i][j] != 'B': # 홀수칸이 B라고 가정했는데 B가 아니면
                        cnt += 1
        count.append(min([cnt, 64-cnt]))

print(min(count))