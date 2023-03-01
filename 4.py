n = int(input())
k = int(input())
x = int(input())
y = int(input())
var = (x-1)*2+y
v1 = var - k
v2 = var + k
if v1 < 1 and v2 > n:
    print(-1)
elif v1 >= 1 and v2 <= n:
    x1 = (v1 - 1) // 2 + 1
    x2 = (v2 - 1) // 2 + 1
    y1, y2 = v1 % 2, v2 % 2
    if y1 == 0: y1 = 2
    if y2 == 0: y2 = 2
    if x - x1 < x2 - x:
        print(x1, y1)
    else:
        print(x2, y2)
elif v1 >= 1:
    y = v1 % 2
    if y == 0: y = 2
    print((v1-1)//2+1, y)
elif v2 <= n:
    y = v2 % 2
    if y == 0: y = 2
    print((v2 - 1) // 2 + 1, y)
