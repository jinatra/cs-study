import sys

word = sys.stdin.readline().rstrip().upper()

d = {}

for w in word:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

max_val = max(d.values())
max_char = [k for k, v in d.items() if v == max_val]

print(max_char[0] if len(max_char) == 1 else '?')