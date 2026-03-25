import sys

A, B = map(str, sys.stdin.readline().split())
rev_a = ''
rev_b = ''

for i in A:
    rev_a = i + rev_a
for i in B:
    rev_b = i + rev_b

print(max([int(rev_a), int(rev_b)]))