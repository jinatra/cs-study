import sys

word = sys.stdin.readline().strip()
rev = word[::-1]

print(1 if word == rev else 0)