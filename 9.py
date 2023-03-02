N, M, K = map(int, input().split())
a = [[i for i in map(int, input().split())] for j in range(N)]
b = [[0 for i in range(M+1)] for j in range(N+1)]
for i in range(1, N+1):
    ans = 0
    for j in range(1, M+1):
        ans += a[i-1][j-1]
        b[i][j] = ans + b[i-1][j]
# for i in range(N+1):
#     print(*b[i])
# print()
for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    ans = b[x2][y2]-b[x2][y1-1]-b[x1-1][y2]+b[x1-1][y1-1]
    print(ans)
