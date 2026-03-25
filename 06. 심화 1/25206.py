import sys

dic = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

grades = []
for _ in range(20):
    info = sys.stdin.readline().rstrip().split()
    credit = info[1]
    rating = info[2]
    if rating != 'P':
        grades.append((credit, rating))

nums = []
for credit, rating in grades:
    if rating in dic:
        rating = dic[rating]
        nums.append((float(credit), rating))


x = 0
credits = 0

for credit, rating in nums:
    x += (credit * rating)
    credits += credit

print(x/credits)

