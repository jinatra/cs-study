import sys

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

a, b = map(int, sys.stdin.readline().rstrip().split())
print(int(a * b/gcd(a, b)))
