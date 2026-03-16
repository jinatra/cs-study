# a, b, c = map(int, input().split())

# mx_num = max([a, b, c])

# if a == b == c:
#     print(10000+a*1000)
# elif a == b:
#     print(1000+a*100)
# elif a == c:
#     print(1000+a*100)
# elif b == c:
#     print(1000+b*100)
# else:
#     print(mx_num*100)
    

a, b, c = map(int, input().split())

l = [a,b,c]
s = set(l)

if len(s) == 1:
    print(10000+a*1000)
elif len(s) == 2:
    two = max(l, key=l.count)
    print(1000+two*100)
else:
    print(max(l)*100)