import sys

def check(input):
    if input.startswith(')'):
        return 'NO'
    stack = []
    for i in input:
        if i == '(':
            stack.append(i)
        if i == ')':
            if not stack:
                return 'NO'
            stack.pop()
    if not stack:
        return 'YES'
    else:
        return 'NO'

def check2(s):
    count = 0
    for c in s:
        if c == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return 'NO'
        return 'YES' if count == 0 else 'NO'

T = int(sys.stdin.readline())
for _ in range(T):
    n = str(sys.stdin.readline().rstrip())
    print(check(n))