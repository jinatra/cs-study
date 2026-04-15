import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
la = set(list(map(int, sys.stdin.readline().rstrip().split())))
lb = set(list(map(int, sys.stdin.readline().rstrip().split())))

print(len(la.difference(lb)) + len(lb.difference(la)))