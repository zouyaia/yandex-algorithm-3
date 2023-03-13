m, n = map(int, input().split())
dp = [[-1 for i in range(n+1)] for j in range(m+1)]
dp[1][0] = 1
dp[0][1] = 1
dp[0][0] = 1
for i in range(m):
    for j in range(n):
        if dp[i][j] != -1: continue
        if i != 0 and j != 0:
            dp[i][j] = dp[i-1][j]+dp[i][j-1]+dp[i-1][j-1]
        elif i == 0:
            dp[i][j] = dp[i][j-1]
        elif j == 0:
            dp[i][j] = dp[i - 1][j]
print(dp[m-1][n-1])