import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
c, d = map(int, sys.stdin.readline().rstrip().split())

bj = a * d + c * b
bm = b * d

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

g = gcd(bj, bm)
print(int(bj/g), int(bm/g))