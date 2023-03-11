n, a, b = map(int, input().split())
INF = int(1e9)+7
dp = [INF]*(n+1)
dp[0] = 0
dp[1] = 0
for i in range(2, n+1):
    for k in range(i+1):
        dp[i] = min(dp[i], max(dp[i-k]+a, dp[k]+b))
print(dp[n])