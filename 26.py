def solve(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    ans = 0
    for move in moves:
        x, y = i + move[0], j + move[1]
        if 0 <= x < n and 0 <= y < m:
            ans += solve(x, y)
    dp[i][j] = ans
    return ans


n, m = map(int, input().split())
dp = [[-1 for i in range(m)] for j in range(n)]
dp[0][0] = 1
moves = [[-1, -2], [-2, -1], [-2, 1], [1, -2]]
print(solve(n-1, m-1))
