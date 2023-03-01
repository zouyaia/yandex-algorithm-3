n = int(input())
a = []
for i in range(n):
    x = int(input())
    a += [x]
ans = 0
for i in range(1, n):
    ans += min(a[i], a[i-1])
print(ans)

# 4
# 4 aaaa
# 3 bbb
# 2 cc
# 3 ddd
# 3 eee
# -> 7