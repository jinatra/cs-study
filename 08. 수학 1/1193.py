import sys

X = int(sys.stdin.readline())

# 1 : 1/1                      +1
# 2 : 1/2 2/1                  +2
# 3 : 3/1 2/2 1/3              +3
# 4 : 1/4 2/3 3/2 4/1          +4
# 5 : 5/1 2/4 3/3 2/4 1/5      +5

count = 0
n = 1

while count < X:
    count += n
    n += 1

line = n-1
pos = X - (count - line)  # 그룹 안에서 몇 번째인지
if line % 2 == 1:  # 홀수 그룹: 분자 감소, 분모 증가
    print(f"{line - pos + 1}/{pos}")
else:  # 짝수 그룹: 분자 증가, 분모 감소
    print(f"{pos}/{line - pos + 1}")