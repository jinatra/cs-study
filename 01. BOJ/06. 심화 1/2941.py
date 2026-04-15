import sys

words = sys.stdin.readline().rstrip()

three = 'dz='
cr_alp = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']


words = words.replace(three, 'a')

for a in cr_alp:
    words = words.replace(a, 'a')
    
print(len(words))

