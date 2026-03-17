N = int(input())

times = N // 4
str_list = []

for i in range(times):
    str_list.append('long')
str_list.append('int')

print(' '.join(str_list))