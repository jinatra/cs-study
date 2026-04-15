import sys

def check(input):
    stack = []
    for i in input:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack:
                return 'no'
            if stack[-1] == '(':
                stack.pop()
            else:
                return 'no'
        elif i == ']':
            if not stack:
                return 'no'
            if stack[-1] == '[':
                stack.pop()
            else:
                return 'no'
    if not stack:
        return 'yes'
    else:
        return 'no'

while True:
    s = str(sys.stdin.readline().rstrip())
    if s == '.':
        break
    else:
        print(check(s))