l = []
for i in range(5):
    line = input()
    row = []
    for i in range(len(line)):
        row.append(line[i])
    l.append(row)

max_count = max([len(i) for i in l])

matrix = []
for row in l:
    count = max_count - len(row)
    if count != 0:
        matrix.append(row + ['no']*count)
    else:
        matrix.append(row)

ans = ''


for j in range(max_count):
    for i in range(5):
        if matrix[i][j] is not 'no':
            ans += matrix[i][j]

print(ans)

# [0][0] + [1][0] + [2][0] .. + [4][0] + [5][0]
# [0][1] + [1][1]