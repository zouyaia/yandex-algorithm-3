n = int(input())
dp = [-1]*(n+1)
dp[0] = 0
e = min(n+1, int(n**(1/3))+1)
cubes = [] # 10^3
for i in range(1, e):
    cubes.append(i**3)
for i in cubes:
    for j in 
print(cubes)
print(dp[n])