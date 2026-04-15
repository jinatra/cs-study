import sys

N = int(sys.stdin.readline())
que = []
for _ in range(N):
    ip = str(sys.stdin.readline().rstrip())
    if ip.startswith('push'):
        c, n = ip.split()
    else:
        c = ip
    
    if c == 'push':
        que.append(n)
    elif c == 'pop':
        if not que:
            print(-1)
        else:
            print(que[0])
            del que[0]
    elif c == 'size':
        print(len(que))
    elif c == 'empty':
        print(1) if not que else print(0)
    elif c == 'front':
        print(que[0]) if que else print(-1)
    else: #back
        print(que[-1]) if que else print(-1)