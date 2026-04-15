A, B, C = map(int, input().split())
D = A%C
E = B%C

print((A+B)%C)
print((D + E)%C)
print((A*B)%C)
print((D * E)%C)