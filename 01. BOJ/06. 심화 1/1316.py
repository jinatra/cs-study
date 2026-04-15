import sys

N = int(sys.stdin.readline())

ans = N
for _ in range(N):
    word = sys.stdin.readline().strip()
    s = set()
    for i in range(1, len(word)):
        # 지금 문자가 이전 문자랑 같으면
        if word[i] == word[i-1]:
            # set에 추가
            s.add(word[i])
        # 지금 문자가 이전 문자랑 틀리면
        else:
            # set에 있으면
            if word[i] in s:
                # 그룹문자가 아니니까 하나 빼기
                ans -= 1
                break
            # set에 없으면
            else:
                # set에 추가
                s.add(word[i-1])
print(ans)