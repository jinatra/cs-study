# 4 -> [] -> 스택 비어있으니 1
# 1 3 -> [3]
# 1 5 -> [3, 5]
# 3 -> [3, 5] -> 정수 갯수 2
# 2 -> [3, 5] -> 맨위 정수 5 빼고 출력 -> 5
# 5 -> [5]


import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    inp = sys.stdin.readline().rstrip()
    if inp.startswith('1'):
        n, x = map(int, inp.split())
    else:
        n = int(inp)
    
    if n == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if n == 1:
        stack.append(x)
    if n == 3:
        print(len(stack))
    if n == 2:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    if n == 5:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])