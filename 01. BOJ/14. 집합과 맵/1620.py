import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

dic_name = {}
dic_num = {}
for i in range(N):
    name = sys.stdin.readline().rstrip()
    dic_name[name] = i+1
    dic_num[i+1] = name

for _ in range(M):
    info = sys.stdin.readline().rstrip()
    if info.isdigit(): # 숫자면 
        print(dic_num[int(info)])
    else:
        print(dic_name[info])