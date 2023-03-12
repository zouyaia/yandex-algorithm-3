a = input()
b = input()
n, m = len(a)+1, len(b)+1
dp = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        if i==j==0: dp[i][j] = 0
        elif j == 0 and i > 0: dp[i][j] = i
        elif i == 0 and j > 0: dp[i][j] = j
        else: dp[i][j] = min(dp[i][j-1]+1, min(dp[i-1][j]+1, dp[i-1][j-1]+int(a[i-1]!=b[j-1])))
print(dp[n-1][m-1])