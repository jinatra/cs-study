import sys
import math

A, B, V = map(int, sys.stdin.readline().rstrip().split())

# 매일 올라가는 길이
du = (A - B)

d = math.ceil((V-A) / (A -B) + 1)

print(d)