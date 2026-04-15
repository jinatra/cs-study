# [1,2,3,4,5,6,7] []
# [1,2,4,5,6,7] [3]


import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

nums = []
for i in range(N):
    nums.append(i+1)

# K = 3
ans = []
current = K - 1 # 2
while len(nums) > 0:
    # 값 뽑을 인덱스 찾기
    # K가 3일 경우 인덱스는 2임
    idx = current % len(nums) # 2
    pick = nums[idx]
    ans.append(pick)
    nums.remove(pick)
    current = idx + K - 1

a = ', '.join(map(str, ans))
print('<'+ a + '>')