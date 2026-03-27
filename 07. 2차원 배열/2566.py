import sys

nums = []
for i in range(9):
    row = list(map(int, input().split()))
    nums.append(row)

big = 0
x = 0
y = 0
for i in range(9):
    for j in range(9):
        if nums[i][j] >= big:
            big = nums[i][j]
            x = i+1
            y = j+1

print(big)
print(x, y)

