import sys

S = sys.stdin.readline().rstrip()

s =set()
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        s.add(S[i:j])

print(len(s))