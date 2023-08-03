n,m = map(int, input().split())

dp = []
dp.append([0] * (m+2))

for _ in range(n):
    dp.append([0] + list(map(int,input().split())) + [0])
dp.append([0] * (m+2))

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] += max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[n][m])