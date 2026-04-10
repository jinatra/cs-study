import sys

N = int(sys.stdin.readline())
cards_dic = {}
for c in map(int, sys.stdin.readline().split()):
    if c in cards_dic:
        cards_dic[c] += 1
    else:
        cards_dic[c] = 1

M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
ans = []
for n in nums:
    if n in cards_dic:
        ans.append(str(cards_dic[n]))
    else:
        ans.append(str(0))

print(' '.join(ans))