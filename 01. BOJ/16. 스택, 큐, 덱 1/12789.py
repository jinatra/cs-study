import sys

# 5 1 3 2 4
# [5]
# [5 3]

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

stack = []
cnt = 1
for i in nums:
    if i == cnt:
        cnt += 1
    else:
        stack.append(i)
    # 스택이 차있고, 마지막이 cnt랑 같으면
    while stack and stack[-1] == cnt:
        stack.pop() # 꺼내서 집어넣고
        cnt += 1 # 카운트 1 올리고

if not stack:
    print('Nice')
else:
    print('Sad')