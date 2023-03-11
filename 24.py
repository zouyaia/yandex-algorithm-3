n = int(input())
C = 32400
lt = []
tr = []
t = [0]*(C+1)
dp = [-1]*(C+1)
for i in range(n):
    tm, tme = input().split()
    tm = list(map(int, tm.split(':')))
    tm = tm[0]*3600+tm[1]*60+tm[2]-C
    tme = int(tme)
    lt.append(tm)
    tr.append(tme)
lt.append(C) # 18:00:00
tr.append(C)
# print(*lt)
# print(*tr)
j = 0
for i in range(C+1):
    if i == lt[j+1]:
        j += 1
    t[i] = tr[j]
# print(*t)
dp[0] = 0
break_st, break_fi = 13*3600-C, 14*3600-C
for i in range(C+1):
    if break_st < i < break_fi:
        continue
    elif i == break_st:
        dp[i] = max(dp[i], dp[i-1])
        continue
    elif i == break_fi:
        dp[i] = dp[break_st]
    elif i != 0:
        dp[i] = max(dp[i], dp[i-1])
    if i+t[i] < C+1 and not(i <= break_st and i+t[i]>=break_fi):
        dp[i+t[i]] = max(dp[i+t[i]], dp[i]+1)
print(dp[C])